from jarvis_run import db, logger
from flask_sqlalchemy import SQLAlchemy
from flask import request
from jarvis.models.users import Users

"""
Various helper utilities for working with the DB
get_roles:  Get user roles
insert_ticket:  Add tickets to the tickertqueue
update_ticket:  Update ticketqueue entry
add_user:  Add user to users table
add_team:  Add team stuff to authorized_teams
"""


