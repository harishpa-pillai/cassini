import logging


class CLogger:

    @staticmethod
    def log_gen():
        # Create a custom logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # Create handler
        console_handler = logging.StreamHandler()

        # Create formatters and add it to handlers
        c_format = logging.Formatter("[%(asctime)s] - [%(levelname)s] - %(message)s - [%(filename)s] ",
                                     "%Y-%m-%d %H:%M:%S")
        console_handler.setFormatter(c_format)

        # Add handlers to the logger
        if logger.hasHandlers():
            logger.handlers.clear()

        logger.addHandler(console_handler)
        logger.propagate = False
        return logger
