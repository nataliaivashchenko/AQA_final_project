from add_db_group import create_group, get_group_name
from page_object import main_page
from page_object.main_page import MainPage


# def test_admin_page(main_page):
#     admin_page = main_page.open_admin_page()
#     admin_page.admin_login()
#     assert admin_page.site_text().text == 'Django administration'


def test_admin_page(main_page):
    admin_page = main_page.open_admin_page()
    assert admin_page.site_text().text == 'Django administration'


# def test_add_group(main_page):
#     admin_page = main_page.open_admin_page()
#     admin_page.admin_login()
#     admin_page.open_groups()
#     assert admin_page.open_groups.text == 'test_group'


def test_add_group(chrome_driver, db):
    create_group(db, 'test_group')
    # page = MainPage(chrome_driver)
    # page.open()
    admin_page = main_page.open_admin_page()
    admin_page.open_groups()
    assert admin_page.open_groups.text == 'test_group'


def test_change_group(chrome_driver, db):
    page = MainPage(chrome_driver)
    page.open()
    admin_page = page.open_admin_page()
    groups_page = admin_page.open_groups()
    group = admin_page.open_first_group()
    change_group = group.change_group_name()
    get_group_name(db)
    assert admin_page.open_groups.text == 'test_group2'
