from django.core.management.base import BaseCommand
from optparse import make_option
import sys

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--noinput', action='store_false', dest='interactive', default=True,
            help='Tells Django to NOT prompt the user for input of any kind.'),
        make_option('--coverage', action='store_false', dest='coverage', default=False,
                    help='Tells Django to run the coverage runner'),
    )
    help = 'Runs the test suite for the specified applications, or the entire site if no apps are specified.'
    args = '[appname ...]'

    requires_model_validation = False

    def handle(self, *test_labels, **options):
        from django.conf import settings
        from django.test.utils import get_runner

        verbosity = int(options.get('verbosity', 1))
        interactive = options.get('interactive', True)
        coverage = options.get('coverage', False)
        test_runner = get_runner(settings, coverage=coverage)

        failures = test_runner(test_labels, verbosity=verbosity, interactive=interactive)
        if failures:
            sys.exit(failures)
