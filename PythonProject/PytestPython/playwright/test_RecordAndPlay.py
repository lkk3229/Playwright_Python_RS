import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_role("textbox", name="email@example.com").click()
    page.get_by_role("textbox", name="email@example.com").fill("lkk3229@gmail.com")
    page.get_by_role("textbox", name="enter your passsword").click()
    page.get_by_role("textbox", name="enter your passsword").fill("Lkk@3229")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name=" Add To Cart").first.click()
    page.get_by_role("button", name=" Add To Cart").nth(1).click()
    page.get_by_role("button", name="   Cart").click()
    page.get_by_role("button", name="❯").nth(4).click()
    page.get_by_role("button", name="Continue Shopping❯").click()
    page.get_by_role("button", name=" Add To Cart").nth(1).click()
    page.get_by_role("button", name="   Cart").click()
    page.get_by_role("button", name="Checkout❯").click()
    page.get_by_role("textbox", name="Select Country").click()
    page.get_by_role("textbox", name="Select Country").fill("India")
    time.sleep(1)
    #page.get_by_role("button", name=" India").click()
    page.get_by_role("textbox").nth(1).click()
    page.get_by_role("textbox").nth(1).fill("523")
    page.get_by_role("textbox").nth(2).click()
    page.get_by_role("textbox").nth(2).fill("Text")
    page.get_by_text("Place Order").click()
    #expect(page.get_by_role("heading", name="Please Enter Full Shipping Information")).to_be_visible()
    #expect(page.locator("h1")).to_contain_text("Please Enter Full Shipping Information")

    # ---------------------
    context.close()
    browser.close()



