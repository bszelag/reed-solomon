class Error(Exception):
    pass


class DivideByZeroException(Error):
    def __init__(self, message):
        self.message = message


class AlphasFromDifferentField(Error):
    def __init__(self):
        self.message = "Alpha elements are from different GF"
