import logging
import functools


class Logger(object):

    def __init__(self, **kwargs):
        self.logger = logging.getLogger(kwargs.get('Name', 'default'))
        self.log_arguments_with_annotation = False
        self.log_return_with_annotation = False

    def __call__(self, fn):
        @functools.wraps(fn)
        def decorated(*args, **kwargs):
            try:
                if self.log_arguments_with_annotation:
                    self.logger.debug(f"{fn.__name__} - {args} - {kwargs}")
                else:
                    self.logger.debug(f"{fn.__name__}")
                result = fn(*args, **kwargs)
                if self.log_return_with_annotation:
                    self.logger.debug(result)
                return result
            except Exception as ex:
                self.logger.debug(f"Exception {ex}")
                raise ex
            return result
        return decorated

    def log(self, level, log):
        getattr(self.logger, level)(log)
