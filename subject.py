class Subject:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __str__(self):
        return f"Subject: {self.name}, Code: {self.code}"

    def __repr__(self):
        return f"Subject(name={self.name}, code={self.code})"
