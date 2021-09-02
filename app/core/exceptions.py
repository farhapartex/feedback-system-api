class CommonException(Exception):
    def __init__(self, details):
        self.details = details


class QueryExecutionFailException(CommonException):
    pass