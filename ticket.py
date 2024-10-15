class Ticket:
    def __init__(self, text, extra_questions, signed_by_dean=False):
        self.text = text
        self.extra_questions = extra_questions
        self.signed_by_dean = signed_by_dean

    def __eq__(self, other):
        if isinstance(other, Ticket):
            return self.text == other.text and self.signed_by_dean == other.signed_by_dean
        return False

    def __str__(self):
        return f"Ticket: {self.text}, Extra questions: {self.extra_questions}, Signed by Dean: {self.signed_by_dean}"

    def __repr__(self):
        return f"Ticket(text={self.text}, signed_by_dean={self.signed_by_dean})"
