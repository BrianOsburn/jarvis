"""
Simple check to see if the app is functioning
"""

from flask import Flask,abort, jsonify, request
from jarvis import app
from jarvis_run import logger


@app.route('/echo', methods=['GET', 'POST'])
def echo():
    logger.info("Echo function called")
    logger.info(request.form)
    echo_message = {'text':  'Echo Completed'}
    return jsonify(echo_message)

