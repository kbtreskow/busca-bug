import requests
from dotenv import load_dotenv
import os

load_dotenv()

def send_logs(message):
    webhook_url = os.getenv('WEBHOOK')
    webhook_url = webhook_url.replace("\\x3a", ":")
    mensaje = {"content": message}
    requests.post(webhook_url, json=mensaje)
