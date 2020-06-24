# Import libraries
from flask import Flask, jsonify, abort, make_response, request
import atexit

# Import required files
from data import groups, relays
from setGroup import setGroup
from setRelay import setRelay
from pwmControl import setPWMBoard

# Initialize PWM boards by setting all outputs to 0
def initPWM():
    for relayPin in range(16):
        setPWMBoard(0, relayPin, 0)
        setPWMBoard(1, relayPin, 0)

initPWM()

# If application exits -> set all outputs to 0
atexit.register(initPWM)

# Define Flask application
app = Flask(__name__)
# Disable Flask JSON sorting
app.config['JSON_SORT_KEYS'] = False
# Enable JSON pretty print
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Returns all items in the "groups" array as JSON
@app.route('/groups', methods=['GET'])
def getGroups():
    return jsonify({'groups': groups})

# Returns all items in the "relays" array as JSON
@app.route('/relays', methods=['GET'])
def getRelays():
    return jsonify({'relays': relays})

# Returns single group item as JSON
@app.route('/groups/<int:groupID>', methods=['GET'])
def getGroup(groupID):
    group = [group for group in groups if group['id'] == groupID]
    if len(group) == 0:
        abort(404)
    return jsonify({'group': group[0]})

# Returns single relay item as JSON
@app.route('/relays/<int:relayID>', methods=['GET'])
def getRelay(relayID):
    relay = [relay for relay in relays if relay['id'] == relayID]
    if len(relay) == 0:
        abort(404)
    return jsonify({'relay': relay[0]})

# Updates a single item in the group array
@app.route('/groups/<int:groupID>', methods=['PUT'])
def updateGroup(groupID):
    # Get the group array with the requested ID
    group = [group for group in groups if group['id'] == groupID]

    # DOWN, UP or STOP are valid positions to be set
    allowedPositions = ["DOWN", "UP", "STOP"]

    # Check if group exists
    if len(group) == 0:
        abort(404)

    # Check if request is valid JSON
    if not request.json:
        abort(400)

    # Check if setPosition is a string
    if 'setPosition' in request.json and type(request.json['setPosition']) != str:
        abort(400)

    # Check if setPosition is allowed to be set
    if request.json['setPosition'] not in allowedPositions:
        abort(400)

    # If the value which should be set is already set, set STOP, else pass the new value
    if request.json.get('setPosition') == group[0]['setPosition']:
        group[0]['setPosition'] = "STOP"
    else:
        group[0]['setPosition'] = request.json.get('setPosition')

    # Set the group with the requested values
    setGroup(groupID, group[0]['setPosition'])

    # Return the new group position as JSON
    return jsonify({'group': group[0]['setPosition']})

# Updates a single item in the relay array
@app.route('/relays/<int:relayID>', methods=['PUT'])
def updateRelay(relayID):
    # Get the relay array with the requested ID
    relay = [relay for relay in relays if relay['id'] == relayID]

    # ON or OFF is a valid state to be set
    allowedStates = ["ON", "OFF"]

    # Check if relay exists
    if len(relay) == 0:
        abort(404)

    # Check if request is valid JSON
    if not request.json:
        abort(400)

    # Check if setState is a string
    if 'setState' in request.json and type(request.json['setState']) != str:
        abort(400)

    # Check if setState is allowed to be set
    if request.json['setState'] not in allowedStates:
        abort(400)

    # Set the data value as the requested value
    relay[0]['setState'] = request.json.get('setState')

    # Set the relay with the requested values
    setRelay(relayID, relay[0]['setState'])

    # Return the new relay state as JSON
    return jsonify({'relay': relay[0]['setState']})

# Return software info
@app.route('/info', methods=['GET'])
def getInfo():
    return jsonify({'version': 'v1.6'})

# If Flask has a 404, return a JSON error message
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'ID not found!'}), 404)

# Start the Flask application
if __name__ == '__main__':
    app.run()
