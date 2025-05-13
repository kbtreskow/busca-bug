from dotenv import load_dotenv
import os

from playwright.sync_api import sync_playwright, Playwright

from dc import send_logs
from test_login import test_login_google, test_login_azure
from test_select_assistant import test_select_assistant
from test_load_data import test_load_data
from test_mesage import test_mesage

load_dotenv()
url= os.getenv('URL')
url = url.replace("\\x3a", ":")

name_step = 'test_inicio'
def run(playwright: Playwright):
    try:
        send_logs("Iniciando recorrido de pruebas en FactorIA")
        chromium = playwright.chromium
        browser = chromium.launch(headless=True)
        page = browser.new_page()
        page.on("console", lambda msg: (print(f"[CONSOLE ERROR] {msg.text}"), send_logs(f"```diff\n- [CONSOLE ERROR] {name_step}\n  {msg.text}```")) if msg.type == "error" else None)
        page.goto(url)
        page.wait_for_load_state()

        name_step = 'test_login_google'
        test_login_google(page)
          
        name_step = 'test_select_assistant'
        test_select_assistant(page)
        
        name_step = 'test_load_data'
        test_load_data(page)
        
        name_step = 'test_mesage'
        test_mesage(page)
        

    except Exception as ex:
        send_logs(f"--Error bot Proceso de [run]: {ex}")
        print(f"--Error bot Proceso de [run]: {ex}")


with sync_playwright() as playwright:
    run(playwright)
