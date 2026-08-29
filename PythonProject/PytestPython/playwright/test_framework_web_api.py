import json
#pytest --browser_name chrome -m smoke -n 3 --html=report.html --tracing retain-on-failure
import pytest
from playwright.sync_api import Playwright, expect

from pageObjects.login import LoginPage
from utils.apiBaseFramework import APIUtils

#JSON file -> util -> access into test
with open('data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']


@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright: Playwright, user_credentials, browserInstance):
    userName = user_credentials['userEmail']
    password = user_credentials['userPassword']

    #create order --> orderId
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)

    loginPage = LoginPage(browserInstance)  #object for LoginPage
    loginPage.navigate()
    dashboardPage = loginPage.login(userName, password)

    orderHistoryPage = dashboardPage.selectOrdersNavLink()
    orderDetailsPage = orderHistoryPage.selectOrder(orderId)
    orderDetailsPage.verifyOrderMessage()
    #orders History name -> order is present




