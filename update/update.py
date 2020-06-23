import os

os.system('cd /home/pi/relay-control/app && rm -rf *')

os.system('cd /home/pi/ && wget https://github.com/AUThomasCH/relay-control/releases/latest/download/relay-control.zip && unzip -o relay-control && rm relay-control.zip')

os.system('service relay-control-app start')

raise SystemExit