from exception import InvalidGradeException

class Exam:
    def __init__(self, start_date, schedule_end_date, tickets, teacher, subject):
        self.start_date = start_date
        self.schedule_end_date = schedule_end_date
        self.tickets = tickets
        self.teacher = teacher
        self.subject = subject
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def set_grade(self, student, grade):
        if student in self.students:
            student.grades[self.subject] = grade
        else:
            raise InvalidGradeException(f"Student {student.name} is not enrolled in the exam.")

    def __str__(self):
        return f"Exam for {self.subject} by {self.teacher.name} on {self.start_date}"

    def __repr__(self):
        return f"Exam(subject={self.subject}, teacher={self.teacher.name}, start_date={self.start_date})"
