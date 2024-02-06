import logging
import os
import inspect


class LogGen:
    @staticmethod
    def loggen():
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.dirname(current_dir)
        log_file = os.path.join(project_dir, 'Logs', 'logfile.log')
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger
