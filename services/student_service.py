from models.student import Student

class StudentService:
    def __init__(self):
        self.students = []
    
    def add_student(self, name, age, student_id):
        student = Student(name, age, student_id)
        self.students.append(student)
        return student
    
    def list_students(self):
        return [s.introduce() for s in self.students]