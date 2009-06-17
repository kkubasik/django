# Generated by the windmill services transformer
from windmill.authoring import WindmillTestClient

# def test_recordingSuite0():
#     client = WindmillTestClient(__name__)
#     client.open("http://localhost:8000/test_admin/admin")
#     client.type(text="Hello", name='q')
#     client.click(xpath=u"//span[@id='body']/center/form/table[2]/tbody/tr[8]/td")
#     client.waits.forPageLoad(timeout=u'20000')
#     client.asserts.assertNode(xpath=u"//div[@id='res']/div/ol/li/h3[1]/a/em")
#     client.asserts.assertNode(link=u'How do you say hello in Japanese ? - Yahoo! Answers')
#     client.asserts.assertNode(link=u'hello')
#     client.asserts.assertNode(link=u'japanese')
#


def test_recordingSuite1():
    client = WindmillTestClient(__name__)

    # print dir(client)
    #    print dir(client.open)
    #    print dir(client.commands)
    #    print client.commands()

    client.open(url="http://localhost:8000/test_admin/admin")
    client.type(text=u'super', id=u'id_username')
    client.type(text=u'secret', id=u'id_password')
    client.click(value=u'Log in')
    client.waits.forPageLoad(timeout=u'20000')
    client.asserts.assertNode(xpath=u"//div[@id='content-main']/div/table/tbody/tr[1]/th")
    client.asserts.assertNode(link=u'Articles')
    client.asserts.assertNode(link=u'Add')
    client.asserts.assertNode(link=u'Change')
    client.asserts.assertNode(link=u'Admin_Views')
    client.asserts.assertNode(xpath=u"//div[@id='user-tools']/strong")
    client.click(xpath=u"//div[@id='content-main']/div/table/tbody/tr[22]/td/a")
    client.waits.forPageLoad(timeout=u'20000')
    client.type(text=u'Test Section', id=u'id_name')
    client.click(name=u'_save')
    client.waits.forPageLoad(timeout=u'20000')
    client.asserts.assertNode(link=u'Section object')
    client.click(link=u'         Admin_views       ')
    client.waits.forPageLoad(timeout=u'20000')
    client.waits.forElement(link=u'Add', timeout=u'8000')
    client.click(link=u'Add')
    client.waits.forPageLoad(timeout=u'20000')
    client.type(text=u'Test 1', id=u'id_title')
    client.type(text=u'This is test content.', id=u'id_content')
    client.click(link=u'Today')
    client.click(link=u'Now')
    client.click(id=u'id_section')
    client.select(option=u'Section object', id=u'id_section')
    client.click(value=u'1')
    #client.asserts.assertValue(validator=u'2009-06-16', id=u'id_date_0')
    #client.asserts.assertValue(validator=u'13:31:21', id=u'id_date_1')
    client.asserts.assertNode(id=u'id_section')
    client.click(name=u'_save')
    client.waits.forPageLoad(timeout=u'20000')
    client.asserts.assertNode(link=u'This is test content.')
    client.asserts.assertNode(xpath=u"//div[@id='changelist']/form/table/tbody/tr/td[2]")
    client.asserts.assertNode(xpath=u"//div[@id='changelist']/form/table/tbody/tr/td[3]")
    client.asserts.assertNode(xpath=u"//div[@id='changelist']/form/table/tbody/tr/td[4]")
    client.asserts.assertNode(xpath=u"//div[@id='changelist']/form/table/tbody/tr/td[5]")
    client.asserts.assertNode(xpath=u"//div[@id='changelist']/form/table/tbody/tr/th")
    client.click(link=u'Today')
    client.waits.forPageLoad(timeout=u'20000')
    client.asserts.assertNode(xpath=u"//div[@id='changelist']/form/table/tbody/tr/th")
    client.click(link=u'        Home       ')
    client.waits.forPageLoad(timeout=u'20000')