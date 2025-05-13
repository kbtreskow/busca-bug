from dc import send_logs
from dotenv import load_dotenv
import os

load_dotenv()
path_test_pdf = os.getenv('PDFPATH')

def test_load_data(e):
    try:
        with e.expect_file_chooser() as fc_info:
            e.get_by_role("button", name="Archivos").click()
            
        file_chooser = fc_info.value
        file_chooser.set_files(path_test_pdf)
        e.wait_for_selector('span.truncate:text("test_pdf.pdf")')
        elemento_cargado = e.query_selector('span.truncate:text("test_pdf.pdf")')
        #if elemento_cargado:
            #send_logs(f"--Archivo cargado: {elemento_cargado.inner_text()}")
            #print(f"--Archivo cargado: {elemento_cargado.inner_text()}")
        e.wait_for_timeout(5000)
        
    except Exception as ex:
        send_logs(f"```diff\n- [BOT ERROR] test_load_data:\n  {ex}```")
        print(f"--Error bot Proceso de [test_load_data]: {ex}")