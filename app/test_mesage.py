from dc import send_logs

def test_mesage(e):
    try:
        e.locator('textarea[placeholder="Envia un mensaje"]').fill("Hola, en que me puedes ayudar?")
        #send_logs("--Mensaje escrito")
        #print("--Mensaje escrito")

        e.get_by_role("button", name="Envia un mensaje").click()
        e.wait_for_selector('p:has-text("Hola, en que me puedes ayudar?")')
        mensaje_enviado = e.query_selector('p:has-text("Hola, en que me puedes ayudar?")')
        #if mensaje_enviado:
            #send_logs(f"--Mensaje enviado: {mensaje_enviado.inner_text()}")
            #print(f"--Mensaje enviado: {mensaje_enviado.inner_text()}")

        e.wait_for_timeout(5000)
        
        caja_mensajes = e.locator('div.animate-slide-up')
        if caja_mensajes.count() > 1:
            respuesta_asistente = caja_mensajes.nth(2).locator('div > div > div:nth-child(2) > div > div > p > button')
            respuesta = respuesta_asistente.inner_text()
            #send_logs(f"--Respuesta asistente: {respuesta}")
            #print(f"--Respuesta asistente: {respuesta}")


    except Exception as ex:
        send_logs(f"```diff\n- [BOT ERROR] test_mesage:\n  {ex}```")
        print(f"--Error bot Proceso de [test_mesage]: {ex}")