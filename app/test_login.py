from dc import send_logs
from dotenv import load_dotenv
import os

load_dotenv()
username= os.getenv('USERNAME')
password= os.getenv('PASSWORD')

def test_login_azure(e):
    try:
        e.get_by_label("Acepto los ").check()
        e.wait_for_load_state()

        e.get_by_role("button", name="Tu cuenta de microsoft").click()
        #send_logs("--Pagina de login abierta")
        #print("--Pagina de login abierta")
        e.wait_for_load_state()
    
        e.get_by_label("Email, phone, or skype").fill(username)
        e.get_by_role("button", name="Next").click()
        #send_logs("--Email Ingresado")
        #print("--Email Ingresado")
        e.wait_for_load_state()
    
        e.get_by_label("Enter your password").fill(password)
        e.get_by_role("button", name="Next").click()
        #send_logs("--Password Ingresado")
        #print("--Password Ingresado")
        e.wait_for_timeout(20000)
    except Exception as ex:
        send_logs(f"Error bot Proceso de [test_login]: {ex}")
        print(f"Error bot Proceso de [test_login]: {ex}")
        

def test_login_google(e):
    try:
        e.get_by_label("Acepto los ").check()
        e.wait_for_load_state()

        e.get_by_role("button", name="Tu cuenta de Google").click()
        #send_logs("--Pagina de login abierta")
        #print("--Pagina de login abierta")
        e.wait_for_load_state()
    
        e.get_by_label("Email or phone").fill(username)
        e.get_by_role("button", name="Next").click()
        #send_logs("--Email Ingresado")
        #print("--Email Ingresado")
        e.wait_for_load_state()
    
        e.get_by_label("Enter your password").fill(password)
        e.get_by_role("button", name="Next").click()
        #send_logs("--Password Ingresado")
        #print("--Password Ingresado")
        e.wait_for_timeout(10000)

    except Exception as ex:
        send_logs(f"```diff\n- [BOT ERROR] test_login:\n  {ex}```")
        print(f"--Error bot Proceso de [test_login]: {ex}")