# Relay-Control

Python3 Flask API to control [Adafruit PWM/Servo Drivers](https://learn.adafruit.com/adafruit-16-channel-pwm-slash-servo-shield/overview)


## Setup

### Get the latest Release
cd to /home/pi
```sh
cd /home/pi
```
Download the latest Release from GitHub
```sh
wget https://github.com/AUThomasCH/relay-control/releases/latest/download/relay-control.zip
```
Unzip it
```sh
unzip relay-control.zip
```

### Install dependencies
Install all dependencies via pip3
```sh
pip3 install --upgrade -r relay-control/config/requirements.txt --timeout 999
```

### Setup the Systemd services with Auto-Update from GitHub (optional)
Copy both systemd config files to the systemd path
```sh
cp relay-control/config/relay-control-* /etc/systemd/system
```

Enable the relay-control Auto-Update Service
```sh
sudo systemctl enable relay-control-update.service
```

If you use Auto-Update, don't enable relay-control-app.service! The update service will start it.

Start the relay-control-app
```sh
sudo systemctl start relay-control-app.service
```

Auto-Update will download the latest release every system start.

### Setup the Systemd service without Auto-Update from GitHub (optional)
Copy the systemd config file to the systemd path
```sh
cp relay-control/config/relay-control-app.service /etc/systemd/system
```

Enable the relay-control-app service
```sh
sudo systemctl enable relay-control-app.service
```

Start the relay-control-app
```sh
sudo systemctl start relay-control-app.service
```

## API Usage
### Get the current state of a relay group
- groups/0 defines the ID of the group (0-13)
```sh
curl -i http://127.0.0.1:5000/groups/0
```

Response:
```sh
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 194
Server: Werkzeug/1.0.1 Python/3.7.3
Date: Mon, 15 Jun 2020 22:36:14 GMT

{
  "group": {
    "id": 0,
    "board": 0,
    "setPosition": "DOWN",
    "relays": {
      "UP": {
        "relayPin": 0
      },
      "DOWN": {
        "relayPin": 1
      }
    }
  }
}
```

### Change the group position (control relays in the relay group)
- groups/0 defines the ID of the group (0-13)
- "setPosition":"DOWN" defines, which relay of the relay group should be set (UP, DOWN or STOP)
```sh
curl -i -H "Content-Type: application/json" -X PUT -d '{"setPosition":"DOWN"}' http://127.0.0.1:5000/groups/0
```

Response:
```sh
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 22
Server: Werkzeug/1.0.1 Python/3.7.3
Date: Mon, 15 Jun 2020 22:35:22 GMT

{
  "group": "DOWN"
}
```

### Get the current state of a relay which is not in a relay group
- relays/0 defines the ID of the relay (0-3)
```sh
curl -i http://127.0.0.1:5000/relays/0
```

Response:
```sh
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 95
Server: Werkzeug/1.0.1 Python/3.7.3
Date: Mon, 15 Jun 2020 22:38:38 GMT

{
  "relay": {
    "id": 0,
    "board": 1,
    "relayPin": 12,
    "setState": "OFF"
  }
}
```

### Change the relay state of a relay which is not in a relay group
- relays/0 defines the ID of the relay (0-3)
- "setState":"ON" defines the state (ON or OFF)
```sh
curl -i -H "Content-Type: application/json" -X PUT -d '{"setState":"ON"}' http://127.0.0.1:5000/relays/0
```

Response:
```sh
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 20
Server: Werkzeug/1.0.1 Python/3.7.3
Date: Mon, 15 Jun 2020 22:40:43 GMT

{
  "relay": "ON"
}
```

### Get the complete relay array
```sh
curl -i http://127.0.0.1:5000/relays
```

Response:
```sh
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 404
Server: Werkzeug/1.0.1 Python/3.7.3
Date: Mon, 15 Jun 2020 22:42:23 GMT

{
  "relays": [
    {
      "id": 0,
      "board": 1,
      "relayPin": 12,
      "setState": "OFF"
    },
    {
      "id": 1,
      "board": 1,
      "relayPin": 13,
      "setState": "OFF"
    },
    {
      "id": 2,
      "board": 1,
      "relayPin": 14,
      "setState": "OFF"
    },
    {
      "id": 3,
      "board": 1,
      "relayPin": 15,
      "setState": "OFF"
    }
  ]
}
```

### Get the complete groups array
```sh
curl -i http://127.0.0.1:5000/groups
```

Response:
```sh
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 2958
Server: Werkzeug/1.0.1 Python/3.7.3
Date: Mon, 15 Jun 2020 22:42:56 GMT

{
  "groups": [
    {
      "id": 0,
      "board": 0,
      "setPosition": "DOWN",
      "relays": {
        "UP": {
          "relayPin": 0
        },
        "DOWN": {
          "relayPin": 1
        }
      }
    },
    {
      "id": 1,
      "board": 0,
      "setPosition": "STOP",
      "relays": {
        "UP": {
          "relayPin": 2
        },
        "DOWN": {
          "relayPin": 3
        }
      }
    },
    .....
  ]
}
```

### Get the Software Information
```sh
curl -i http://127.0.0.1:5000/info
```

Response:
```sh
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 24
Server: Werkzeug/1.0.1 Python/3.7.3
Date: Tue, 23 Jun 2020 14:34:05 GMT

{
  "version": "vX.X"
}

```

## License

relay-control is open source software
[licensed as GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
