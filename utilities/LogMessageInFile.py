import logging
import time


class LogMessageInFile:

    def log_message_into_file(self, message, type_of_log):

        print(type_of_log)
        print(message)

        logger = logging.getLogger()
        file_name = 'Logs//TestAmazonMiniTv.log'

        file_handler = logging.FileHandler(file_name)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :% (name)s: % (message)s")

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)

        # logging.basicConfig(
        #     filename=file_name,
        #     filemode='w',
        #     format='%(asctime)s: %(levelname)s:%(message)s',
        #     level=logging.DEBUG
        # )

        if type_of_log.__eq__("debug"):
            logging.debug(message)

        elif type_of_log.__eq__("info"):
            logging.info(message)

        elif type_of_log.__eq__("warning"):
            logging.warning(message)

        elif type_of_log.__eq__("error"):
            logging.error(message)

        elif type_of_log.__eq__("critical"):
            logging.critical(message)
