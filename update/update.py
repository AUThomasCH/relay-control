import os
import fs
from fs import open_fs
import gnupg
import socket

gpg = gnupg.GPG()

try:
    socket.create_connection(("github.com", 443))
    print("Connection to GitHub ok.")

    os.system('cd /home/pi/ && wget https://github.com/AUThomasCH/relay-control/releases/latest/download/relay-control.zip.gpg')

    fileStream = open('/home/pi/relay-control.zip.gpg', "rb")
    signature = gpg.verify_file(fileStream)

    if signature.status == "signature valid":
        print("Signature is valid!")

        with open('/home/pi/relay-control.zip.gpg', 'rb') as f:
            status = gpg.decrypt_file(
                file=f,
                output='/home/pi/relay-control.zip',
            )

        print(status.stderr)

        os.system('rm -rf /home/pi/relay-control/app/*')
        os.system('unzip -o -d /home/pi /home/pi/relay-control.zip')
        os.system('rm /home/pi/relay-control.zip*')

    else:
        print("Signature invalid or missing!")

except Exception as e:
    print(str(e))

finally:
    os.system('service relay-control-app start')
    raise SystemExit
