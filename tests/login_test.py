import allure
import pytest

from base.base_test import BaseTest


@allure.feature('Login testing')
class TestLogin(BaseTest):
    @allure.title('Login')
    @allure.severity('Critical')
    def test_login(self):
        """ Checks if user is logged in and Dashboard page is opened """

        self.login_page.login(self.data.EMAIL, self.data.PASSWORD)
        self.dashboard_page.is_opened()
        self.dashboard_page.is_logged_in()
        self.login_page.make_screenshot('Successful login')
