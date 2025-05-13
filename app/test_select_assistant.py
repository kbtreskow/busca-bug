from dc import send_logs
import random

def test_select_assistant(e):
    try:
        e.wait_for_selector('ul.p-4 li')
        ul_list = e.locator('ul.p-4 li').all()
        assitant_random = random.choice(ul_list)
        e.get_by_role("button", name = assitant_random.inner_text()).click()
        e.wait_for_load_state()
        #send_logs(f"--Asistente seleccionado: {assitant_random.inner_text()}")
        #print(f"--Asistente seleccionado: {assitant_random.inner_text()}")
        e.wait_for_timeout(5000)
    except Exception as ex:
        send_logs(f"```diff\n- [BOT ERROR] test_select_assistant:\n  {ex}```")
        print(f"--Error bot Proceso de [test_select_assistant]: {ex}")