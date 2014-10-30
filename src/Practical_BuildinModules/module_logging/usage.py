__author__ = 'wenychan'

import logging
import logging.config

# The logging library takes a modular approach and offers several
# categories of components: loggers, handlers, filters, and formatters.
#
# Loggers expose the interface that application code directly uses.
# Handlers send the log records (created by loggers) to the appropriate destination.
# Filters provide a finer grained facility for determining which log records to output.
# Formatters specify the layout of log records in the final output.



logging.config.fileConfig('logging.conf')

# If logging.raiseExceptions is False, the event is silently dropped.
# If logging.raiseExceptions is True, a message 'No handlers could be found for logger X.Y.Z' is printed once.
logging.raiseExceptions = 0

def usage():
    # create logger
    logger = logging.getLogger('simpleExample')

    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')

def usage1():
    # create logger
    logger = logging.getLogger('simpleExample')

    # dynamically set logger
    # CRITICAL/ERROR/WARNING/INFO/DEBUG/NOTSET
    logger.setLevel(logging.ERROR)

    # dynamically add/remove handler
    # logger.addHandler()
    # logger.removeHandler()

    # dynamically add/remove filter
    # logger.addFilter()
    # logger.removeFilter()

    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')

def usage2():
    # other logger methods
    # create logger
    logger = logging.getLogger('simpleExample')

    # creates a log message similar to Logger.error().
    # The difference is that Logger.exception() dumps a
    # stack trace along with it. Call this method only
    # from an exception handler.
    # logger.exception()

    # akes a log level as an explicit argument.
    # This is a little more verbose for logging messages
    # than using the log level convenience methods listed
    # above, but this is how to log at custom log levels.
    logger.log()

def usage3():
    # Useful handlers

    # In addition to the base Handler class, many useful subclasses are provided:
        # StreamHandler instances send messages to streams (file-like objects).
        # FileHandler instances send messages to disk files.
        # BaseRotatingHandler is the base class for handlers that rotate log files at a certain point. It is not meant to be instantiated directly. Instead, use RotatingFileHandler or TimedRotatingFileHandler.
        # RotatingFileHandler instances send messages to disk files, with support for maximum log file sizes and log file rotation.
        # TimedRotatingFileHandler instances send messages to disk files, rotating the log file at certain timed intervals.
        # SocketHandler instances send messages to TCP/IP sockets.
        # DatagramHandler instances send messages to UDP sockets.
        # SMTPHandler instances send messages to a designated email address.
        # SysLogHandler instances send messages to a Unix syslog daemon, possibly on a remote machine.
        # NTEventLogHandler instances send messages to a Windows NT/2000/XP event log.
        # MemoryHandler instances send messages to a buffer in memory, which is flushed whenever specific criteria are met.
        # HTTPHandler instances send messages to an HTTP server using either GET or POST semantics.
        # WatchedFileHandler instances watch the file they are logging to. If the file changes, it is closed and reopened using the file name. This handler is only useful on Unix-like systems; Windows does not support the underlying mechanism used.
        # NullHandler instances do nothing with error messages. They are used by library developers who want to use logging, but want to avoid the ‘No handlers could be found for logger XXX’ message which can be displayed if the library user has not configured logging. See Configuring Logging for a Library for more information.

    pass

if __name__ == '__main__':
    usage()

    print '#'*30

    usage1()