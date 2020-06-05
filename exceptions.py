class AdbNotFound(Exception):
    pass


class InvalidParameter(Exception):
    pass


class EventExecutionFailed(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message


class UnknownAction(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message
