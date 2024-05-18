import pytest
from pages.login_page import LoginPage
from pages.post_creation_page import PostCreationPage
from pages.dashboard_page import DashboardPage
from cfg.data import Data


class BaseTest:
    data: Data
    login_page: LoginPage
    dashboard_page: DashboardPage
    post_creation_page: PostCreationPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.post_creation_page = PostCreationPage(driver)
