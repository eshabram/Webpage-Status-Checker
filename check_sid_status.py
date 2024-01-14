import time
import os
import subprocess
import requests

def send_notification(title, message):
    # Use PowerShell to display a toast notification
    ps_script = f'powershell -Command "New-BurntToastNotification -Text \'{message}\'"'
    subprocess.Popen(ps_script, shell=True)

def ping(address):
    request = requests.get('https://www.spaceisdirty.com')
    return request.ok

if __name__ == "__main__":
    while True:
        site_up = ping("www.spaceisdirty.com")
        if not site_up:
            send_notification("Server Down", "spaceisdirty.com is down!")

        time.sleep(600)
