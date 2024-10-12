class InvalidGradeException(Exception):
    def __init__(self, message="Invalid grade!"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message
