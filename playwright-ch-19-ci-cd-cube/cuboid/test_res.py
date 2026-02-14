from playwright.sync_api import sync_playwright, Page, expect
import pytest

BASE_URL = "http://127.0.0.1:8000/#!"


def test_extract_results(page: Page):
    # open the url
    page.goto(BASE_URL)
    cub = page.get_by_role("link", name="cuboid")
    assert cub.is_visible() == True

    '''
    rest = page.locator("//h3[text()]")
    ct = rest.count()
    print("\nCount:", ct)
    print("Status:", rest.nth(0))
    print("Status:", rest.nth(1))
    print("Status:", rest.nth(2))
    '''
    '''
    for i in ct.range(0,3):
        print(rest.nth(i).inner_text)
    assert ct > 0
    '''
