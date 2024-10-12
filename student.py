from human import Human


class Student(Human):
    def __init__(self, name, age, group):
        super().__init__(name, age)
        self.group = group

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, Group: {self.group}"

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}, group={self.group})"
