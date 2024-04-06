import allure
from awwwards_tests.models.models import Profile


@allure.story('Log in')
def test_login():
    page = Profile()
    page.open()
    page.login()
