from services.student_service import StudentService
from utils.file_manager import FileManager

def run():
    service = StudentService()
    service.add_student("Avinash", 28, "S101")
    service.add_student("Riya", 22, "S102")

    students = service.list_students()
    print("\n".join(students))

    FileManager.save_to_file("students.json", students)

if __name__ == "__main__":
    run()