"""
Simple check to see if the app is functioning
"""

from flask import Flask,abort, jsonify, request
from jarvis import app
from jarvis_run import logger


@app.route('/heartbeat', methods=['GET', 'POST'])
def heartbeat():
    logger.info("Heartbeat function called")
    heartbeat_message = {'text':  'I\'m Alive'}
    return jsonify(heartbeat_message)

