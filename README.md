Python SDET Automation Framework

A beginner-built test automation framework using Python, Pytest, Playwright, and HTTPX.

Features

- UI automation tests using Playwright
- Login testing with multiple test scenarios
- API testing using HTTPX
- Reusable Pytest fixtures
- Shared API assertion helpers
- HTML test reports using pytest-html
- One-command test execution using PowerShell

Tech Stack

- Python
- Pytest
- Playwright
- HTTPX
- pytest-html

Project Structure

python-sdet-framework/
pages/login_page.py
tests/test_login.py
/test_api.py
/api_helpers.py
conftest.py
.gitignore
run_tests.ps1
README.md

Run the Tests

Activate the virtual environment:

.\.venv\Scripts\Activate.ps1

Run all tests and generate the HTML report:

.\run_tests.ps1

The report is generated as "report.html" in the project root.

Test Environments

- UI tests: SauceDemo demo website
- API tests: JSONPlaceholder public test API

This project is for learning and demonstrating test automation skills.