import allure
from base.base_page import BasePage
from cfg.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class DashboardPage(BasePage):
    PAGE_URL = Links.ADMIN_DASHBOARD
    SEARCH_INPUT = (By.TAG_NAME, 'input')
    TABLE_ROW = (By.CSS_SELECTOR, 'tbody tr')

    @allure.step('Searching for title')
    def search_for_title(self, title):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_INPUT)).send_keys(title)

    @allure.step('Checking table emptiness')
    def check_table_emptiness(self):
        self.wait.until(EC.visibility_of_element_located(self.TABLE_ROW))
