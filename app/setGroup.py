# Import libraries
from data import groups
from pwmControl import setPWMBoard
import time

def setGroup(groupID, setPosition):
    # Get the group array with the requested ID
    group = [group for group in groups if group['id'] == groupID]

    # Get the board, relayPinDown and relayPinUp from the data array
    board = group[0]['board']
    relayPinDown = group[0]['relays']['DOWN']['relayPin']
    relayPinUp = group[0]['relays']['UP']['relayPin']

    if setPosition == "DOWN":
        # Disable the mutual relay pin
        setPWMBoard(board, relayPinUp, 0)
        # Wait some time for security reason
        time.sleep(0.5)
        # Enable the PWM output
        setPWMBoard(board, relayPinDown, 65535)

    elif setPosition == "UP":
        # Disable the mutual relay pin
        setPWMBoard(board, relayPinDown, 0)
        # Wait some time for security reason
        time.sleep(0.5)
        # Enable the PWM output
        setPWMBoard(board, relayPinUp, 65535)

    elif setPosition == "STOP":
        # Disable the up and down PWM output
        setPWMBoard(board, relayPinUp, 0)
        setPWMBoard(board, relayPinDown, 0)

    else:
        pass
