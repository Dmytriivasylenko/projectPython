from student import Student

class Group:
    def __init__(self, number):
        self.number = number
        self.students = []

    def add_student(self, student):
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