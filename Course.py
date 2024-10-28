from Student import Student


class Course:
    course_name: str
    course_code: str
    instructor: str
    students: list

    def __init__(self, course_name: str, course_code: str, instructor: str):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self,
                    student: 'Student') -> None:  #student: 'Student' indicates student parameter should be an instance of the Student class.
        if student.student_id not in self.students:
            self.students.append(
                student.student_id)  #we dont wanna append the entire class rather just the id to identify the students

    def display_course_info(self) -> None:
        print(f"Course Name: {self.course_name}")
        print(f"Course Code: {self.course_code}")
        print(f"Instructor: {self.instructor}")
        print("Enrolled Students:")
        print("Students:", ", ".join(self.students))

    def to_dict(self):
        return {
            "course_name": self.course_name,
            "course_code": self.course_code,
            "instructor": self.instructor,
            "students": self.students
        }

    @staticmethod
    def save_courses_to_json(courses, filename="Course"):  #default name Course
        course_list = [course.to_dict() for course in courses]
        with open(filename, 'w') as json_file:
            import json
            json.dump(course_list, json_file, indent=4)

    @staticmethod
    def load_courses_from_json(path):
        with open(path, 'r') as json_file:
            import json
            courses_data = json.load(json_file)

            courses: list[Course] =[]  # students is a list student object (we need to initialize it

            for course_data in courses_data:
                course = Course(
                    course_data["course_name"],
                    course_data["course_code"],
                    course_data["instructor"]
                )
                course.students = course_data["students"]
                courses.append(course)

            return courses



