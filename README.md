Python SDET Automation Framework

A Python-based test automation framework built using Pytest, Playwright, and HTTPX. This project demonstrates UI automation, API testing, reusable test components, and automated test reporting.

Features

- Browser-based UI automation using Playwright
- Login testing with valid and invalid credentials
- Shopping cart testing (add and remove products)
- End-to-end checkout flow testing
- REST API testing using HTTPX
- Reusable Pytest fixtures
- Page Object Model (POM) implementation
- Shared API assertion helpers
- Parameterized test cases
- HTML test reports using pytest-html
- PowerShell script for one-command test execution

Tech Stack

Technology| Purpose
Python| Programming language
Pytest| Test framework
Playwright| Browser automation
HTTPX| API testing
pytest-html| HTML test reporting
Git & GitHub| Version control

Project Structure

- "pages/" – Page Object Model classes
- "tests/" – UI, API, cart and checkout tests
- "tests/api_helpers.py" – Reusable API validation functions
- "conftest.py" – Shared Pytest fixtures
- "run_tests.ps1" – Test execution and HTML report generation
- ".gitignore" – Files excluded from Git
- "README.md" – Project documentation

Test Coverage

UI Tests – SauceDemo

- Login with valid credentials
- Login with invalid credentials
- Login with blank credentials
- Add products to the shopping cart
- Remove products from the shopping cart
- Complete the checkout process

API Tests – JSONPlaceholder

- Retrieve user information using GET
- Validate user response data
- Verify non-existent user responses
- Test multiple user IDs
- Create a user using POST
- Validate response status and content

Running the Tests

1. Activate the virtual environment

.\.venv\Scripts\Activate.ps1

2. Run the complete test suite

python -m pytest -v

3. Generate the HTML test report

.\run_tests.ps1

The HTML report is generated as "report.html" in the project root.

Test Environments

- UI testing: SauceDemo demo application
- API testing: JSONPlaceholder public testing API

Current Test Results

15 automated test cases passing

The framework is continuously being improved as part of practical SDET learning and development.

---

This project is intended for learning and demonstrating Python-based software test automation skills.