"""
This is the coach API server.

It is ready to run as a cloudfroundry deployment,
just change the "run_locally" variable to "False".

The response messages are all formated in JSON.

The API endpoints are following routes:
    / :
        a welcome message
    /match_ids :
        returns all available match IDs
    /first_blood/<match_id> :
        returns the first blood event of the given match_id
    /kill_sequences/<match_id> :
        returns all kill sequences of the given match_id
    /intensity/<match_id> :
        returns the intensity series of the given match_id
    /match_duration/<match_id> :
        returns the match duration of the given match_id
"""

import os
import json
from flask import Flask, make_response
import pandas as pd

import player_api as player_api


# If this api is not deployed on cloudfoundry make sure that run_locally is
# set to True, it will run on localhost:5000
run_locally = True

# Create the application instance
app = Flask(__name__)


if run_locally:
    port = 5000
else:
    port = int(os.getenv("PORT"))


# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the root URL
    Return:
        Welcome Message
    """
    response = make_response("Hello!", 200)
    return response


@app.route("/player_long/<player_id>")
def get_player_long(player_id):
    player_id = int(player_id)
    player = player_api.get_player_long(player_id)
    response = make_response(player.to_json(), 200)
    return response


@app.route("/player_short/<player_id>")
def get_player_short(player_id):
    player_id = int(player_id)
    player = player_api.get_player_short(player_id)
    response = make_response(player.to_json(), 200)
    return response


@app.route("/base/<base_id>")
def get_base(base_id):
    base_id = int(base_id)
    base = player_api.get_base(base_id)
    response = make_response(base.to_json(), 200)
    return response


@app.route("/formation_ids")
def get_formation_ids():
    formation_ids = player_api.get_formation_ids()
    formation_ids = {"formation_ids": formation_ids}
    response = make_response(json.dumps(formation_ids), 200)
    return response


@app.route("/formation/<formation_id>")
def get_formation(formation_id):
    formation = player_api.get_formation(formation_id)
    formation = {"formation": formation}
    response = make_response(json.dumps(formation), 200)
    return response


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    if run_locally:
        app.run(debug=True)
    else:
        app.run(host='0.0.0.0', port=port, debug=False)
