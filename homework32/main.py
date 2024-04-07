
from group import Group
from exception import TooManyStudentsError
from student import Student

group = Group("PD1")
for i in range(10):
    student = Student(f"Student{i+1}", "Smith")
    group.add_student(student)

try:
    student_11 = Student("Student11", "Smith")
    group.add_student(student_11)
except TooManyStudentsError as e:
    print(e)

print(group)
