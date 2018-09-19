# -*- coding:  utf-8 -*-

"""
Python slack bot.  Stolen from https://github.com/slackapi/Slack-Python-Onboarding-Tutorial/blob/master/bot.py
"""

#import os
from slackclient import SlackClient
from jarvis_run import app_config


class Bot(object):
    """
    Initialize things
    """
    def __init__(self):
        super(Bot, self).__init__()
        self.name = "Jarvis"
        self.emoji = ":cloud:"

        self.oauth = {"client_id": app_config['slack']['client_id'],
                      "client_secret": app_config['slack']['client_secret'],
                      "scope": "bot"}
        self.verification = app_config['slack']['slack_signing_secret']

        self.client = SlackClient("")

        self.messages = {}

    def bot_auth(self, code):
        """
        Authenticate with OAuth and assign correct scopes to the bot
        authorized teams will be added to the DB once it's done
        :param code:
        :return:
        """

        #logger.info("Starting up Bot")

        auth_response = self.client.api.call(
            "oauth.access",
            client_id=self.oauth["client_id"],
            client_secret=self.oauth["client_secret"],
            code=code
        )

        authed_teams = auth_response["team_id"]
        authed_teams[team_id] = {"bot_token":
                                 auth_response["bot"]["bot_access_token"]}

        #logger.info("Connecting to Slack Now...")
        self.client = SlackClient(authed_teams[team_id]["bot_token"])


