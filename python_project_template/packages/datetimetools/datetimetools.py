from datetime import datetime, timedelta
import logging

# Import logger
log = logging.getLogger(__name__)


def get_current_timestamp():
    log.info("Start datetimetools module")
    current_timestamp = str(datetime.now().strftime("%Y-%m-%d__%H-%M-%S"))
    log.info("Finished datetimetools module")
    return current_timestamp


def get_today_date(output_format='%Y-%m-%d'):
    return datetime.now().strftime(output_format)


def get_past_date(days_count, output_format='%Y-%m-%d'):
    tday_date = datetime.now()
    past_date = timedelta(days=days_count)
    return (tday_date - past_date).strftime(output_format)
