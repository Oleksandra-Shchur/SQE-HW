import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.dirname(current_dir)
        log_path = os.path.join(project_dir, 'Logs', 'automation.log')
        logger = logging.getLogger()

        logging.basicConfig(filename=log_path,
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        logger.addHandler(console_handler)
        return logger


