from pytz import timezone
from datetime import datetime


def generate_timestamp():
    """
    Generates timestamp for insertion into the DB in epoch format
    Timezone is set to pacific time for standardization
    :return timestamp, current_time:
    """

    pacific_time = timezone('America/Los_Angeles')
    current_time = datetime.now(pacific_time)
    timestamp = current_time.timestamp()

    return timestamp, current_time
