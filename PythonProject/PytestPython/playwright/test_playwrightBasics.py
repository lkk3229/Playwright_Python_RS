import time

from playwright.sync_api import Page, expect, Playwright


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")

# chromium headless mode, 1 single context
def test_playwrightShortCut(page :Page):
    page.goto("https://www.google.com")

# for CSS => #id or .className or tagName
def test_coreLocators(page :Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractice")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("Learnibng@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    #Incorrect username/password - assertion
    time.sleep(5)


def test_firefoxBrowser(playwright:Playwright):
    page = playwright.firefox.launch(headless=False).new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractice")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("Learnibng@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    # Incorrect username/password - assertion
    time.sleep(5)
