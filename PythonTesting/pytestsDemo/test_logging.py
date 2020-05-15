import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    logger.addHandler(fileHandler)

    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")
    logger.info("Information Statement")
    logger.warning("Something is in warning mode")
    logger.error("A Major error has occurred")
    logger.critical("Critical issue")
