from faker import Faker
from student import Student
from teacher import Teacher
from group import Group
from exam import Exam
from subject import Subject
from ticket_generator import TicketGenerator
from ticket import Ticket

fake = Faker()

student1 = Student(fake.name(), fake.random_int(min=18, max=25), "Group 1")
student2 = Student(fake.name(), fake.random_int(min=18, max=25), "Group 1")

teacher = Teacher(fake.name(), fake.random_int(min=30, max=60), "Mathematics")

ticket1 = Ticket(fake.sentence(), [fake.sentence() for _ in range(2)], signed_by_dean=True)
ticket2 = Ticket(fake.sentence(), [fake.sentence() for _ in range(2)], signed_by_dean=False)

subject = Subject("Mathematics", "MTH101")
exam = Exam(fake.date(), fake.date(), [ticket1, ticket2], teacher, subject)

ticket_generator = TicketGenerator([ticket1, ticket2])
ticket_generator.to_csv("tickets.csv")
ticket_generator.to_json("tickets.json")

group = Group("Group 1")
group.add_student(student1)
group.add_student(student2)

group.notify("Exam is scheduled for next week.")
group.kick(student2)
