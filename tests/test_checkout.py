from playwright.sync_api import expect


def test_complete_checkout(page):
    # Login
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("Products")).to_be_visible()

    # Add a product
    page.get_by_role("button", name="Add to cart").first.click()

    # Open cart
    page.locator(".shopping_cart_link").click()

    expect(page.locator(".cart_item")).to_have_count(1)

    # Start checkout
    page.get_by_role("button", name="Checkout").click()

    expect(page.get_by_text("Checkout: Your Information")).to_be_visible()

    # Enter customer information
    page.get_by_placeholder("First Name").fill("Test")
    page.get_by_placeholder("Last Name").fill("User")
    page.get_by_placeholder("Zip/Postal Code").fill("560001")

    page.get_by_role("button", name="Continue").click()

    # Verify order overview
    expect(page.get_by_text("Checkout: Overview")).to_be_visible()
    expect(page.locator(".cart_item")).to_have_count(1)

    # Finish checkout
    page.get_by_role("button", name="Finish").click()

    # Verify order confirmation
    expect(page.get_by_text("Thank you for your order!")).to_be_visible()