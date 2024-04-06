import allure
from awwwards_tests.models.models import Profile


@allure.story('Checking courses in academy')
def test_academy():
    page = Profile()
    page.open()
    page.check_coursers()
