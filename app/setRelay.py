# Import libraries
from data import relays
from pwmControl import setPWMBoard

def setRelay(relayID, setState):
    # Get the relay array with the requested ID
    relay = [relay for relay in relays if relay['id'] == relayID]

    # Get the board and relayPin from the data array
    board = relay[0]['board']
    relayPin = relay[0]['relayPin']

    if setState == "ON":
        # Enable the PWM output on ON command
        setPWMBoard(board, relayPin, 65535)

    elif setState == "OFF":
        # Disable the PWM output on OFF command
        setPWMBoard(board, relayPin, 0)

    else:
        pass
