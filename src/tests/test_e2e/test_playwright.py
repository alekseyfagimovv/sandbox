from playwright.sync_api import Page, expect


def test_e2e_request(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("WrongPassword!")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("#flash")).to_contain_text("invalid")
    page.screenshot(path="example.png")
