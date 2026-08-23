from playwright.sync_api import Page, expect


def test_UIValidationDynamicScript(page:Page):
    #iphone X, Nokia Edge -> verify 2 items are showing in cart
    page.goto("https://rahulshettyacademy.com/loginpagePractice")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button").click()
    iphoneProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    iphoneProduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")

    with page.expect_popup() as newPage_info:
        #step1
        page.locator('a:has-text("Free Access to InterviewQues/ResumeAssistance/Material")').click()  #new page
        childPage = newPage_info.value
        text = childPage.locator(".red").text_content()
        print(text)   #Please email us at mentor@rahulshettyacademy.com with below template to receive response
        words = text.split("at")  #Please email us,  mentor@rahulshettyacademy.com with below template to receive response
        email = words[1].strip().split(" ")[0]   #0->mentor@rahulshettyacademy.com
        assert email == "mentor@rahulshettyacademy.com"
