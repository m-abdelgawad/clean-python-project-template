import os
import yaml
from packages.project import absolute_path
from packages.logger import logger
from packages.timestamp import timestamp


def main():

    # Initiate logger
    project_abs_path = os.path.dirname(absolute_path.get())
    logs_file_path = logger.create_log_file(
        app_name='project-name', project_abs_path=project_abs_path
    )
    log = logger.setup_app_logger(logger_name='', log_file_path=logs_file_path)

    log.info('Start program execution')

    # Import configurations
    config_path = os.path.join(absolute_path.get(), 'conf.yaml')
    with open(config_path) as config_file:
        conf = yaml.safe_load(config_file)

    # Start testing logger
    log.info('Configuration Username: ' + conf['account']['username'])
    log.info('Configuration Password: ' + conf['account']['password'])
    current_timestamp = timestamp.get_current()
    log.info('Current Timestamp: ' + current_timestamp)
    # Finished testing logger

    log.info('Finished program execution')


if __name__ == '__main__':
    main()
