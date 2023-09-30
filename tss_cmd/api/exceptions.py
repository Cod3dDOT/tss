class ApiException(Exception):
    def __init__(self, code, message="TSS API EXCEPTION OCCURRED"):
        self.code = code
        self.message = message
        super().__init__(self.message)


class ParseException(Exception):
    def __init__(self, message="FAILED PARSING TSS PAGE"):
        self.message = message
        super().__init__(self.message)
