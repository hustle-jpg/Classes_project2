class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def kick(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"{student.name} has been kicked out of the group {self.name}.")
        else:
            print(f"Student {student.name} is not in this group.")

    def pay(self, student, amount):
        if student in self.students:
            print(f"{student.name} has paid {amount} for the group {self.name}.")
        else:
            print(f"Student {student.name} is not in this group.")

    def notify(self, message):
        for student in self.students:
            print(f"Notification to {student.name}: {message}")

    def __len__(self):
        return len(self.students)

    def __contains__(self, student):
        return student in self.students

    def __iter__(self):
        return iter(self.students)

    def __str__(self):
        return f"Group: {self.name}, Students: {[str(student) for student in self.students]}"

    def __repr__(self):
        return f"Group(name={self.name})"
