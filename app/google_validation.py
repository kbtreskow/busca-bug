"""from playwright.sync_api import sync_playwright, Playwright
from dotenv import load_dotenv
import os

load_dotenv()
username= os.getenv('USERNAME')
password= os.getenv('PASSWORD')
url_validation_google= os.getenv('URL_VALIDATION_GOOGLE')
path_test_pdf = os.getenv('PDFPATH')


def login_validation_google(e):
    try:
        e.get_by_label("Email or phone").fill(username)
        e.get_by_role("button", name="Next").click()
        e.wait_for_load_state()

        e.get_by_label("Enter your password").fill(password)
        e.get_by_role("button", name="Next").click()
        e.wait_for_load_state()
    except Exception as ex:
        print(f"{ex}")


def validation_google():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto(url_validation_google)
            page.wait_for_timeout(3000)
            login_validation_google(page)
            page.wait_for_timeout(20000)

            # Close the browser
            context.close()
            browser.close()
    except Exception as ex:
        print(f"Error bot Proceso de [login_google]: {ex}")
"""





"""# google_validation.py

from dotenv import load_dotenv
import os

load_dotenv()
username= os.getenv('USERNAME')
password= os.getenv('PASSWORD')
url_validation_google= os.getenv('URL_VALIDATION_GOOGLE')

def login_validation_google(e):
    try:
        e.get_by_label("Email or phone").fill(username)
        e.get_by_role("button", name="Next").click()
        e.wait_for_load_state()

        e.get_by_label("Enter your password").fill(password)
        e.get_by_role("button", name="Next").click()
        e.wait_for_load_state()
    except Exception as ex:
        print(f"{ex}")


def validation_google(page):
    try:
        page.goto(url_validation_google)
        page.wait_for_timeout(3000)
        login_validation_google(page)
        page.wait_for_timeout(20000)
    except Exception as ex:
        print(f"Error bot Proceso de [login_google]: {ex}")"""
