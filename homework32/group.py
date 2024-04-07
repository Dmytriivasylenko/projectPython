# group.py

from exceptions import TooManyStudentsError
from student import Student

class Group:
    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.students = []

    def add_student(self, student):
        if len(self.students) >= self.MAX_STUDENTS:
            raise TooManyStudentsError("Too many students in the group!")
        self.students.append(student)

    def delete_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                self.students.remove(student)
                break


    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        student_info = "\n".join(str(student) for student in self.students)
        return f"Group {self.number}:\n{student_info}"
