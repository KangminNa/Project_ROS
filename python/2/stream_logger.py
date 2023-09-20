"""stream_logger.py"""
class StreamLogger:
    def __init__(self):
        import logging
        self.logger = logging.getLogger()
        streamHandler = logging.StreamHandler()
        formatter = logging.Formatter("[%(asctime)s][%(levelname)-8s][%(thread)d|%(threadName)s][%(funcName)s|%(lineno)s] >>> %(message)s")
        streamHandler.setFormatter(formatter)
        self.logger.addHandler(streamHandler)
        self.logger.setLevel(level=logging.DEBUG)

        self.debug = self.logger.debug
        self.info = self.logger.info
        self.warning = self.logger.warning
        self.error = self.logger.error
        self.critical = self.logger.critical
