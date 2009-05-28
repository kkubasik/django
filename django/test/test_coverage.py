import coverage
import os, sys

from django.conf import settings
from django.db.models import get_app, get_apps
from django.test.simple import DefaultTestRunner as base_run_tests

from django.utils.module_tools import get_all_modules
from django.test.coverage_report import html_report

def _get_app_package(app_model_module):
    """
    Returns the app module name from the app model module.
    """
    return '.'.join(app_model_module.__name__.split('.')[:-1])


class BaseCoverageRunner(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        pass

    #----------------------------------------------------------------------
    def run_tests(self, test_labels, verbosity=1, interactive=True,
                  extra_tests=[]):
        """
        Test runner which displays a code coverage report at the end of the
        run.
        """
        #coverage.use_cache(0)
        for e in getattr(settings, 'COVERAGE_CODE_EXCLUDES', []):
            coverage.exclude(e)
        coverage.start()
        brt = base_run_tests()
        results = brt.run_tests(test_labels, verbosity, interactive, extra_tests)
        coverage.stop()

        coverage_modules = []
        if test_labels:
            for label in test_labels:
                label = label.split('.')[0]
                app = get_app(label)
                coverage_modules.append(_get_app_package(app))
        else:
            for app in get_apps():
                coverage_modules.append(_get_app_package(app))

        coverage_modules.extend(getattr(settings, 'COVERAGE_ADDITIONAL_MODULES', []))

        packages, self.modules, self.excludes, self.errors = get_all_modules(
            coverage_modules, getattr(settings, 'COVERAGE_MODULE_EXCLUDES', []),
            getattr(settings, 'COVERAGE_PATH_EXCLUDES', []))

        coverage.report(self.modules.values(), show_missing=1)
        if self.excludes:
            print >> sys.stdout
            print >> sys.stdout, "The following packages or modules were excluded:",
            for e in self.excludes:
                print >> sys.stdout, e,
            print >>sys.stdout
        if self.errors:
            print >> sys.stdout
            print >> sys.stderr, "There were problems with the following packages or modules:",
            for e in self.errors:
                print >> sys.stderr, e,
            print >> sys.stdout
        return results


class ReportingCoverageRunner(BaseCoverageRunner):
    """Reporting"""

    def __init__(self, outdir = None):
        """Constructor"""
        if(outdir):
            self.outdir = outdir
        else:
            # Realistically, we aren't going to ship the entire reporting framework..
            # but for the time being I have left it in.
            self.outdir = getattr(settings, 'COVERAGE_REPORT_HTML_OUTPUT_DIR', 'test_html')
            self.outdir = os.path.abspath(self.outdir)
            # Create directory
            if( not os.path.exists(self.outdir)):
                os.mkdir(self.outdir)


    def run_tests(self, *args, **kwargs):
        """"""
        res = BaseCoverageRunner.run_tests(self, *args, **kwargs)
        html_report(self.outdir, self.modules, self.excludes, self.errors)
        print >>sys.stdout
        print >>sys.stdout, "HTML reports were output to '%s'" %self.outdir

        return res    





