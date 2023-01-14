import os
import yaml
from packages.project import absolute_path
from packages.logger import logger
from packages.timestamp import timestamp


# Initiate logger
project_abs_path = os.path.dirname(absolute_path.get())
# TODO: Change Project Name
logs_file_path = logger.create_log_file(
    app_name='project-name', project_abs_path=project_abs_path
)
log = logger.setup_app_logger(logger_name='', log_file_path=logs_file_path)


def main():

    log.info('Start program execution')

    # Import configurations
    config_path = os.path.join(absolute_path.get(), 'config.yaml')
    with open(config_path) as config_file:
        config = yaml.safe_load(config_file)

    # Start testing logger
    log.info('Configuration Username: ' + config['account']['username'])
    log.info('Configuration Password: ' + config['account']['password'])
    current_timestamp = timestamp.get_current()
    log.info('Current Timestamp: ' + current_timestamp)
    # Finished testing logger

    # raise Exception("Test exception to test the error logging")

    log.info('Finished program execution')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        log.error(e)
