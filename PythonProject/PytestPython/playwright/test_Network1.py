from time import time

import pytest
from playwright.sync_api import Page


fakePayloadOrderResponse = {"data":[], "message": "No Orders"}
# Api call from browser -> api call contact server return back response to browser-> browser use response to generate html
def intercept_response(route):
    route.fulfill(
        json = fakePayloadOrderResponse
    )

@pytest.mark.smoke
def test_Network_1(page : Page):
    # login
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("lkk3229@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Lkk@3229")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="ORDERS").click()

    order_text = page.locator(".mt-4").text_content()
    print(order_text)

