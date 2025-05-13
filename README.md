#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Otras conexiones para logs
#page.on("console", lambda msg: print(f"[CONSOLE] {msg.type}: {msg.text}"))
#page.on("response", lambda response: print(f"[RESPONSE ERROR] {response.status} - {response.url}") if response.status >= 400 else None)
#page.on("pageerror", lambda exc: print(f"[PAGE ERROR] {exc}"))
#page.on("error", lambda exc: print(f"[PAGE ERROR] {exc}"))

#Activa pageerror https://the-internet.herokuapp.com/javascript_error
#Activa response https://httpstat.us/500
#Activa response https://pokeapi.co/api/v2/pokemon/0000

#document.body.innerHTML += '<div style="position:fixed;top:10px;left:10px;background:red;color:white;padding:10px;z-index:9999">Error simulado</div>';