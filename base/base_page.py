import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 2, poll_frequency=.5)

    def open(self):
        with allure.step(f'Open {self.PAGE_URL} page'):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f'Page {self.PAGE_URL} is opened'):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def open_n_wait(self):
        self.open()
        self.is_opened()

    def is_logged_in(self):
        nav = self.driver.find_element(By.CSS_SELECTOR, 'nav ul')
        self.wait.until(EC.visibility_of(nav))

    def get_current_url(self):
        return self.driver.current_url

    def logout(self):
        logout_button = (By.XPATH, '//*[contains(text(),"Logout")]')
        self.wait.until(EC.element_to_be_clickable(logout_button)).click()

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG,
        )

    def do_sleep(self, sec=1):
        time.sleep(sec)
