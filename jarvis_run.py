from jarvis import init_config, init_logging, init_db
from jarvis import app
#import time
#from slackclient import SlackClient

#  Init Configuration
app_config = init_config()

#  Init DB
logger = init_logging()

#  Setting up DB Stuff
logger.info("Setting up DB Connection")

db = init_db(app, app_config)


if __name__ == '__main__':

    app.run(host=app_config['flask']['bind_ip'],
            port=app_config['flask']['port'],
            debug=app_config['flask']['debug'])
