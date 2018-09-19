"""
Adds user to the DB
Usage:  /adduser @name (user|manager)
"""

from flask import jsonify, request, make_response
from jarvis import app
from jarvis_run import logger, db


@app.route('/heartbeat', methods=['GET', 'POST'])
def heartbeat():
    logger.info("Heartbeat function called")
    heartbeat_message = {'text':  'I\'m Alive'}
    return jsonify(heartbeat_message)

