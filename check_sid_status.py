import time
import os
import subprocess

def send_notification(title, message):
    # Use PowerShell to display a toast notification
    ps_script = f'powershell -Command "New-BurntToastNotification -Text \'{message}\'"'
    subprocess.Popen(ps_script, shell=True)

def ping(address):
    return not os.system('ping %s -n 1' % (address,))

if __name__ == "__main__":
    while True:
        site_up = ping("www.spaceisdirty.com")
        if not site_up:
            send_notification("Server Down", "spaceisdirty.com is down!")

        time.sleep(600)
