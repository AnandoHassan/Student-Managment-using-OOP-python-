from typing import Dict, Any

from Person import Person


class Student(Person):
    student_id: str
    grades: dict[str, str]
    courses: list

    def __init__(self, name: str, age: int, address: str, student_id: str):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject: str, grade: str) -> None:
        self.grades[subject] = grade

    def enroll_course(self, course: str) -> None:
        if course not in self.courses:
            self.courses.append(course)

    def display_student_info(self) -> None:
        self.display_person_info()
        print(f"Student ID: {self.student_id}")
        print("Grades:", self.grades)
        print("Courses:", ", ".join(self.courses))

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "age": self.age,
            "address": self.address,
            "student_id": self.student_id,
            "grades": self.grades,
            "courses": self.courses
        }

    @staticmethod
    def save_students_to_json(students, filename="Student") -> None:  #default name Student
        students_list = [student.to_dict() for student in students]
        with open(filename, 'w') as json_file:
            import json
            json.dump(students_list, json_file, indent=4)

    @staticmethod
    def load_students_from_json(path) -> list['Student']:
        with open(path, 'r') as json_file:
            import json
            students_data = json.load(json_file)

            students: list['Student'] =[]  #students is a list student object (we need to initialize it)

            for student_data in students_data:
                student = Student(
                    student_data["name"],
                    student_data["age"],
                    student_data["address"],
                    student_data["student_id"]
                )
                student.grades = student_data["grades"]
                student.courses = student_data["courses"]
                students.append(student)

            return students
