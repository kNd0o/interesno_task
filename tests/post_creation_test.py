import allure
import pytest

from base.base_test import BaseTest


@allure.feature('Post creation testing')
class TestPostCreation(BaseTest):

    @allure.title('Post creation')
    @allure.severity('Critical')
    def test_post_creation(self):
        """ Positive scenario to test if notification is shown and post indeed created """

        # Pre-condition
        self.login_page.login(self.data.EMAIL, self.data.PASSWORD)
        self.dashboard_page.is_opened()
        self.post_creation_page.open_n_wait()

        # Actual test
        self.test_data = 'test123'
        self.post_creation_page.enter_title(self.test_data)
        self.post_creation_page.enter_content(self.test_data)
        self.post_creation_page.enter_author(self.test_data)
        self.post_creation_page.click_submit()
        self.post_creation_page.check_notification()
        self.dashboard_page.open_n_wait()
        self.dashboard_page.search_for_title(self.test_data)
        self.dashboard_page.check_table_emptiness()
