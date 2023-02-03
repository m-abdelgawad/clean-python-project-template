import os
import yaml
import traceback
from packages.file import file
from packages.logger import logger
from packages.datetimetools import datetimetools


# Initiate logger
log = logger.get(app_name='logs', enable_logs_file=False)


def main():

    log.info('Start program execution')

    project_abs_path = file.caller_dir_path()
    print(project_abs_path)

    # Import configurations
    config_path = os.path.join(project_abs_path, 'config.yaml')
    with open(config_path) as config_file:
        config = yaml.safe_load(config_file)

    # Start testing logger
    log.info('Configuration Username: ' + config['account']['username'])
    log.info('Configuration Password: ' + config['account']['password'])
    current_timestamp = datetimetools.get_current_timestamp()
    log.info('Current Timestamp: ' + current_timestamp)
    # Finished testing logger

    # raise Exception("Test exception to test the error logging")

    log.info('Finished program execution')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        log.error(e)
        log.error('Error Traceback: \n {0}'.format(traceback.format_exc()))
