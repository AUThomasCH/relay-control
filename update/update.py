import os
import fs
from fs import open_fs
import gnupg

gpg = gnupg.GPG()

os.system('cd /home/pi/ && wget https://github.com/AUThomasCH/relay-control/releases/latest/download/relay-control.zip')

fileStream = open('/home/pi/relay-control.zip', "rb")
signature = gpg.verify_file(fileStream)

if signature.status == "signature valid":
    print("Signature is valid!")
    os.system('rm -rf /home/pi/relay-control/app/*')
    os.system('unzip /home/pi/relay-control.zip')
    os.system('rm /home/pi/relay-control.zip')
    os.system('service relay-control-app start')
else:
    print("Signature invalid or missing!")
    print("Aborting script execution")


raise SystemExit