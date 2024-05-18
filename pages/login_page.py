import allure
from base.base_page import BasePage
from cfg.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    PAGE_URL = Links.ADMIN_LOGIN
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'password')
    SUBMIT_BUTTON = (By.TAG_NAME, 'button')

    @allure.step('Entering email')
    def enter_email(self, email):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys(email)

    @allure.step('Entering password')
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step('Clicking submit button')
    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def login(self, email, password):
        self.open()
        self.enter_email(email)
        self.enter_password(password)
        self.click_submit()
