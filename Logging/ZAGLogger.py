####################################################################################################################
# IMPORTS
import logging
import os
import sys

from datetime import datetime

from logging.handlers import TimedRotatingFileHandler


####################################################################################################################
# CORE
class LogEntry:
    # ---> CONSTRUCTOR
    def __init__(self, time, name, level, message, filename, lineno):
        """
            It creates a Model of a Log Entry based on ZAGLogger message Format

        :param time: Timestamp in float format -> it will be converted in YYYY - MM - dd  HH:MM:ss
        :param name: Log Instance name
        :param level: Log Level
        :param message: Message to Log
        :param filename: Script Name
        :param lineno: Script Line Number
        """
        timestamp = time
        timestamp_dt = datetime.fromtimestamp(timestamp)
        formatted_date = timestamp_dt.strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
        self.time = formatted_date
        self.name = name
        self.level = level
        self.message = message
        self.filename = filename
        self.lineno = lineno

    # ---> FUNCTIONS
    def to_str(self):
        return (f'{self.time} - [{self.name}] - {self.level} - '
                f'{self.message} ({self.filename}:{self.lineno})')


class ZAGLogger(logging.Formatter):
    # ---> CONSTANTS
    # Color for Log messages
    LOG_COL_RED = "\x1b[31;1m"
    LOG_COL_BOLD_RED = "\x1b[31;1;3;4m"
    LOG_COL_GREEN = "\x1b[32m"
    LOG_COL_YELLOW = "\x1b[33;1;3m"
    LOG_COL_BLUE = "\x1b[34m"
    LOG_COL_MAGENTA = "\x1b[35m"
    LOG_COL_CYANOGEN = "\x1b[36m"
    LOG_COL_GREY = "\x1b[37m"

    LOG_COL_RESET = "\x1b[0m"

    # ---> ATTRIBUTES
    # Log Message Format
    format_str = "%(asctime)s - [%(name)s] - %(levelname)s - %(message)s ( %(filename)s:%(lineno)d )"

    # Formats for each Log Level
    formats = {
        logging.DEBUG: LOG_COL_CYANOGEN + format_str + LOG_COL_RESET,
        logging.INFO: LOG_COL_GREEN + format_str + LOG_COL_RESET,
        logging.WARNING: LOG_COL_YELLOW + format_str + LOG_COL_RESET,
        logging.ERROR: LOG_COL_RED + format_str + LOG_COL_RESET,
        logging.CRITICAL: LOG_COL_BOLD_RED + format_str + LOG_COL_RESET
    }

    # ---> CONSTRUCTOR
    def __init__(self, log_name: str, write_file: bool):
        """
            Constructor

        :param log_name: Log name -> Will be print in console in [LOG_NAME]
        :param write_file: Write a log file if true
        """
        super().__init__(fmt=self.formats[logging.DEBUG], datefmt=None, style='%')
        self.log_name = log_name
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(logging.DEBUG)

        # All messages will be stored in log_entries
        self._log_entries = []

        self.logger.addHandler(self._get_console_handler())

        if write_file:
            self.logger.addHandler(self._get_file_handler())

    # ---> FUNCTIONS
    def _get_console_handler(self):
        """
            Get Console Handler

        :return: console handler
        """

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self)
        return console_handler

    def _get_file_handler(self):
        """
            Get File Handler

        :return: file handler
        """
        log_directory = "log"
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        log_filename = f"{log_directory}/{self.log_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.log"
        file_handler = TimedRotatingFileHandler(filename=log_filename, when='midnight')
        file_handler.setFormatter(self)
        return file_handler

    def format(self, record):
        """
            Returns a Log Record formatted basing on FORMAT Enum and so, severity level of log message

        :param record: Record to log
        :return: Formatted record
        """

        log_fmt = self.formats.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

    def print_log(self, log_level, message):
        """
            Print the message in console and save it into an attribute class list stored

        :param log_level: Standard LOG Level
        :param message: Message to log
        :return: Formatted Record as string
        """

        # Print LOG in console
        self.logger.log(log_level, message)

        # Get an instance of logged record with all its properties
        log_record = logging.makeLogRecord({'msg': message, 'levelname': logging.getLevelName(log_level)})

        # Create the log entry based on logged record and save in the class list
        log_entry = LogEntry(log_record.created, self.log_name, log_record.levelname, log_record.msg,
                             log_record.pathname, log_record.lineno)

        # Store the formatted record and return it as a String
        log_entry_str = log_entry.to_str()
        self._log_entries.append(log_entry_str)
        return log_entry_str

    def get_log_entries(self):
        """
            Return Log Entries

        :return: Log Entries
        """

        return self._log_entries


# ---> EXAMPLE RUN
if __name__ == "__main__":
    zag_logger = ZAGLogger("ZAG Logger", True)
    zag_logger.print_log(logging.DEBUG, "Log message level Debug")
    zag_logger.print_log(logging.INFO, "Log message level Info")
    zag_logger.print_log(logging.WARNING, "Log message level Warning")
    zag_logger.print_log(logging.ERROR, "Log message level Error")
    zag_logger.print_log(logging.CRITICAL, "Log message level Critical")
    zag_logger.print_log(logging.NOTSET, "Log message level Critical")
