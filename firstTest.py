import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.pause()
    page.goto("https://www.demoblaze.com/")
    page.wait_for_load_state("networkidle")
    page.get_by_role("link", name="Log in").click()
    page.locator("#loginusername").click()
    page.locator("#loginusername").fill("admin")
    page.locator("#loginpassword").click()
    page.locator("#loginpassword").fill("admin")
    page.get_by_role("button", name="Log in").click()
    print("Test Completed..!")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


# stop at first failure
# pytest -x
#
# Allow max failure before
# mytest --maxfail=2
#
# To run single test
# pytest -k test_name
#
# To run single file:
# pytest filename.py
#
# to re-run the last failed
# pytest --lf