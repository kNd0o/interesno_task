import allure
from base.base_page import BasePage
from cfg.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class PostCreationPage(BasePage):
    PAGE_URL = Links.ADMIN_CREATE
    POST_TITLE = (By.ID, 'title')
    POST_CONTENT = (By.CSS_SELECTOR, '.ql-editor p')
    POST_AUTHOR = (By.ID, 'author')
    POST_DATE = (By.ID, 'actual-date')
    POST_BUTTON = (By.CLASS_NAME, 'btn')
    POST_POPUP = (By.CLASS_NAME, 'alert-success')
    POST_VALIDATION_FIELDS = (By.TAG_NAME, 'small')

    @allure.step('Entering title')
    def enter_title(self, title_text):
        self.wait.until(EC.element_to_be_clickable(self.POST_TITLE)).send_keys(title_text)

    @allure.step('Entering content')
    def enter_content(self, content_text):
        self.wait.until(EC.presence_of_element_located(self.POST_CONTENT))
        self.driver.execute_script(f'p = document.getElementsByTagName("p");p[0].innerText = "{content_text}";')

    @allure.step('Entering author')
    def enter_author(self, author_text):
        self.wait.until(EC.element_to_be_clickable(self.POST_AUTHOR)).send_keys(author_text)

    @allure.step('Clicking submit button')
    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.POST_BUTTON)).click()

    @allure.step('Check if success-popup is present')
    def check_notification(self):
        self.wait.until(EC.presence_of_element_located(self.POST_POPUP))

    @allure.step('Check for validation fields')
    def check_validation_fields(self):
        self.wait.until(EC.presence_of_all_elements_located(self.POST_VALIDATION_FIELDS))

    @allure.step('Choosing data')
    def choose_date(self):
        pass

    @allure.step('Formating content')
    def format_content(self):
        pass
