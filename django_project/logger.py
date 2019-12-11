import logging


class Logger:
    FORMAT_STR = '%(levelname)s:%(name)s:%(asctime)s:%(funcName)s:%(message)s'
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

    def __init__(self, log_filename: str = None) -> None:
        self.log_filename = log_filename

        # 1. Set the logger name and log level
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.INFO)

        # 2. Define the log formatters
        formatter = logging.Formatter(self.FORMAT_STR, self.DATE_FORMAT)

        # 3. Define logging handlers: writes formatted logging records to disk files
        if self.log_filename:
            self.file_handler = logging.FileHandler(self.log_filename)
            self.file_handler.setLevel(logging.ERROR)  # logs only ERROR to the log file
            self.file_handler.setFormatter(formatter)

        # 4. Define extra logging handlers: writes logging records to the console (optional)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)  # logs only INFO to console (optional)
        console_handler.setFormatter(formatter)

        # 5. Add the specified handler to this logger
        if self.log_filename:
            self.log.addHandler(self.file_handler)
        self.log.addHandler(console_handler)


