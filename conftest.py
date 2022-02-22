import pytest
from selenium.webdriver import Chrome
import psycopg2
from page_object.main_page import MainPage


@pytest.fixture(scope="session")
def chrome_driver():
    chrome_driver = Chrome()
    yield chrome_driver
    chrome_driver.quit()


def main_page(chrome_driver):
    page = MainPage(chrome_driver)
    page.open()
    return page


@pytest.fixture(scope='session')
def postgres_connections():
    connection = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='postgres',
        host='localhost'
    )
    dbs = connection.cursor()
    yield dbs
    connection.close()
