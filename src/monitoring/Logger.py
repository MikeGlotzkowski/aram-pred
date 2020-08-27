import logging
import functools


class Logger(object):

    def __init__(self, **kwargs):
        self.logger = logging.getLogger(kwargs.get('Name', 'default'))

    def __call__(self, fn):
        @functools.wraps(fn)
        def decorated(*args, **kwargs):
            try:
                self.logger.debug(f"{fn.__name__} - {args} - {kwargs}")
                result = fn(*args, **kwargs)
                self.logger.debug(result)
                return result
            except Exception as ex:
                self.logger.debug(f"Exception {ex}")
                raise ex
            return result
        return decorated

    def log(self, level, log):
        getattr(self.logger, level)(log)
