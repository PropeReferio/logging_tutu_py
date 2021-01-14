#Sample file of how to create logger from file.conf

import logging
import logging.config

logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)
logger.debug('This is a debug message (using the logger you loaded from file.conf!)')