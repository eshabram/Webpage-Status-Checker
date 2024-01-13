# Webpage-Status-Checker
A simple status checker for my personal website hosted on my local network. This script is for windows. The problem with hosting websites at home is that sometimes they go down without my ones knowledge. When configured properly, this script will run at startup in the background and check the status per your defined time interval, and send a toast notification when the server is not responding. Mine is every ten minutes.

### Install Dependencies:
To install the dependencies, run this command from this repos home folder:
```
pip3 install -r requirements.txt
```

### Configure and Run:
Pyinstaller should have been installed with the dependencies. Run it in order to convert the script to an executable with these commands:
```
pyinstaller --onefile --noconsole check-sid-status.py
```
This will create some directories and a .spec file. The executable that you need is in the dist/ directory that was just created.

NOTE: It is likely to fail the first time through because of the threat detection Windows has by default. You'll have to go to Virus and Threat Protection menu, go into "manage settings" and then add an "exclusion" for the files or folder. Then run it again.

Create a shortcut for the .exe file by right-clicking it in a file explorer and selecting that option. 

Hit the Windows + R key and type in "shell:startup" and hit enter. Place the shortcut here. 

That's it.
