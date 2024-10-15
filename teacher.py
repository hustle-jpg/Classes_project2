from human import Human


class Teacher(Human):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.groups = []

    def assign_group(self, group):
        self.groups.append(group)

    def __str__(self):
        return f"Teacher: {self.name}, Age: {self.age}, Subject: {self.subject}"

    def __repr__(self):
        return f"Teacher(name={self.name}, age={self.age}, subject={self.subject})"

