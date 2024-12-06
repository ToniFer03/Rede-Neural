import datetime
import os
import logging

def create_folder_for_logs(debug_folder_name):
    """
        Funtion responsible for creating a folder to save the logs based on tha name choosen for the folder

        Parameters
        ----------
        debug_folder_name
            Name choosen for the folder

        Returns
        -------
        folder_path
            Relative path of the folder to be used for the debugs

    """
    current_directory = os.getcwd()
    string = debug_folder_name + "_"
    string2 = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder_name = string + string2
    string = "Logs"
    logs_directory = os.path.join(current_directory, string)
    if not os.path.exists(os.path.join(current_directory, string)):
        os.makedirs(os.path.join(current_directory, string))
    folder_path = os.path.join(logs_directory, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path


def logging_config(debug_folder_name):
    """
        Funtion responsible for creating a folder for the logs, creating a logger for each level and file
        handlers for each log and tests the loggers at the end

        Parameters
        ----------
        debug_folder_name
            The name choosen for the logging folder

        Returns
        -------
        debug_logger
            Logger to be used for the debuging options
        
        warning_logger
            Logger to be used for the warning options

        error_logger
            Logger to be used for the error options

    """
    folder_path = create_folder_for_logs(debug_folder_name)

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    debug_logger = logging.getLogger('debug_logger')
    warning_logger = logging.getLogger('warning_logger')
    error_logger = logging.getLogger('error_logger')

    debug_handler = logging.FileHandler(os.path.join(folder_path, 'debug.log'))
    warning_handler = logging.FileHandler(os.path.join(folder_path, 'warning.log'))
    error_handler = logging.FileHandler(os.path.join(folder_path, 'error.log'))

    debug_handler.setLevel(logging.DEBUG)
    warning_handler.setLevel(logging.WARNING)
    error_handler.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    debug_handler.setFormatter(formatter)
    warning_handler.setFormatter(formatter)
    error_handler.setFormatter(formatter)

    debug_logger.addHandler(debug_handler)
    warning_logger.addHandler(warning_handler)
    error_logger.addHandler(error_handler)

    debug_logger.debug('Debug logger set up')
    warning_logger.warning('Warning logger set up')
    error_logger.error('Error logger set up')

    return debug_logger, warning_logger, error_logger