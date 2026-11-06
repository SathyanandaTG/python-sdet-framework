from playwright.sync_api import expect


def test_add_product_to_cart(page):
    # Navigate to the product page
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Products")).to_be_visible()
    page.get_by_role("button", name="Add to cart").first.click()
    # Verify that the product is added to the cart
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")
    page.locator(".shopping_cart_link").click()
    expect(page.locator(".cart_item")).to_have_count(1)


def test_add_two_products_to_cart(page):
    # Navigate to the product page
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Products")).to_be_visible()
    page.get_by_role("button", name="Add to cart").nth(0).click()
    page.get_by_role("button", name="Add to cart").nth(0).click()
    # Verify that two products are added to the cart
    expect(page.locator(".shopping_cart_badge")).to_have_text("2")
    page.locator(".shopping_cart_link").click()
    expect(page.locator(".cart_item")).to_have_count(2)

def test_remove_product_from_cart(page):
    # Navigate to the product page
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Products")).to_be_visible()
    page.get_by_role("button", name="Add to cart").nth(0).click()
    page.get_by_role("button", name="Add to cart").nth(0).click()
    page.locator(".shopping_cart_link").click()
    expect(page.locator(".cart_item")).to_have_count(2)
    page.get_by_role("button", name="Remove").first.click()
    expect(page.locator(".cart_item")).to_have_count(1)
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

def test_remove_one_product_from_cart(page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("Products")).to_be_visible()

    # Add two different products
    page.get_by_role("button", name="Add to cart").nth(0).click()
    page.get_by_role("button", name="Add to cart").nth(0).click()

    # Open the cart
    page.locator(".shopping_cart_link").click()

    # Confirm both products are present
    expect(page.locator(".cart_item")).to_have_count(2)

    # Remove the first product
    page.get_by_role("button", name="Remove").first.click()

    # Confirm one product remains
    expect(page.locator(".cart_item")).to_have_count(1)
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")