# -*- coding: utf-8 -*-
import os
import sys

from flask import Flask, render_template, redirect, request
from flask_session import Session

"""
Fetch static data
"""
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))



app = Flask(__name__, static_url_path='/static')
sess = Session()
app.config['SESSION_TYPE'] = 'filesystem'
# sess.init_app(app)

# Valid routes
@app.route("/")
def main():
    return "Hello"

@app.route("/verify_facebook")
def verify_facebook():
    VERIFY_TOKEN = "1234553asdcds3"

    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode and token:
        # Verify
        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return challenge

@app.route("/webhook", methods= ["POST"])
def webhook() : 
    if request.method == "POST" : 
        body = request.json
        if body["object"] == "page" : 
            print(1)
            for entry in body["entry"] :
                event = entry["messaging"][0]
                print(event)

                senderId = event["sender"]["id"]
                print("Sender ID " + senderId)
                
                return "Entry Rec",200
        else : 
            return "error",404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
