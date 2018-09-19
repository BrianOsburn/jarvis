# -*- coding:  utf-8 -*-
"""
Processes incoming bot requests (separate from the slash commands)
SHELL FOR NOW
"""

import json
import bot
from flask import Flask, request, make_response, render_template

