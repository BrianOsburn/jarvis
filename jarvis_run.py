from jarvis import init_config, init_logging, init_db, app



#  Init Configuration
app_config = init_config()

#  Init DB
logger = init_logging()

#  Setting up DB Stuff
logger.info("Setting up DB Connection")

db = init_db(app, app_config)

#  Get the routes
import jarvis.routes.heartbeat
import jarvis.routes.echo


#  Init the bot
from jarvis.bot_core import core

jbot = core.Bot()
slack = jbot.client


import jarvis.routes.event_listener



if __name__ == '__main__':

    app.run(host=app_config['flask']['bind_ip'],
            port=app_config['flask']['port'],
            debug=app_config['flask']['debug'])
