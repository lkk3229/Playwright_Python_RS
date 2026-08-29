
from playwright.sync_api import Page, Playwright, expect

from utils.apiBase import APIUtils


def interceptRequest(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4c0b9f6fb0")


def test_Network_2(page : Page):
    # login
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", interceptRequest)
    page.get_by_placeholder("email@example.com").fill("lkk3229@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Lkk@3229")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)

def test_session_storage(playwright :Playwright):
    api_utils = APIUtils()
    getToken = api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #script to insert token in session local storage
    page.add_init_script(f"""localStorage.setItem('token', '{getToken}')""")
    page.goto("https://rahulshettyacademy.com/client/")

    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()




