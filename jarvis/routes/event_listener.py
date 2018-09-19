"""
Listens for events from Slack
"""

from flask import jsonify, request, make_response
from jarvis import app
from jarvis_run import logger, jbot
from jarvis.utilities import validate_call

import json


@app.route('/listener', methods=['POST'])
def listener():
    logger.info("Event Received:")
    slack_event = json.loads(request.data)

    logger.debug(slack_event)

    #  Slack URL Verification
    #  Slack will post a challenge event in order to verify who we are.  This will be how we respond

    if "challenge" in slack_event:
        logger.info("Challenge Received")
        return make_response(slack_event["challenge"], 200, {"content_type":  "application/json"})

    #  Validation that the event is truly from slack
    if not validate_call.validate_request(request):
        logger.critical("Failed message validation!")
        message = "Invalid Slack Token Verification! \nExpected:  %s, \nReceived:  %s" % (slack_event["token"],
                                                                                          jbot.verification)

        make_response(message, 403, {"X-Slack-No-Retry": 1})

    #  Process incoming events
    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        logger.debug("Received event type:  %s", event_type)
        logger.debug("Full event data:  \n %s", slack_event)

    return make_response("[Test] These are not the droids\
                             you're looking for.", 200, {"X-Slack-No-Retry": 1})



