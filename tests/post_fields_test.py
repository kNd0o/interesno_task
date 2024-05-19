import allure
import pytest

from base.base_test import BaseTest


@allure.feature('Post fields testing')
class TestPostCreationFields(BaseTest):

    @allure.title('Post creation fields')
    @allure.severity('Minor')
    def test_post_fields(self):
        """ Checks if validation messages under inputs are shown after focus change """

        # Pre-condition
        self.login_page.login(self.data.EMAIL, self.data.PASSWORD)
        self.dashboard_page.is_opened()
        self.post_creation_page.open_n_wait()

        # Actual test
        self.test_data = ''
        self.post_creation_page.enter_title(self.test_data)
        self.post_creation_page.enter_content(self.test_data)
        self.post_creation_page.enter_author(self.test_data)
        self.post_creation_page.click_submit()
        self.post_creation_page.check_validation_fields()
        self.post_creation_page.make_screenshot('Fields are present')
