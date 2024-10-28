from Student import Student
from Course import Course
import hashlib
import os
import json

def generate_unique_id(input_id):
    input_str = str(input_id).encode()  # Convert the input to a string and encode it
    hash_object = hashlib.sha256()  # Create a SHA-256 hash object
    hash_object.update(input_str)  # Update the hash object with the encoded input
    unique_id = hash_object.hexdigest()  # Get the hexadecimal representation of the hash
    return unique_id

def main():
    students: dict[str, 'Student'] = {}  # List of Students, uniquely identified by student_id
    courses: dict[str, 'Course'] = {}  # List of Courses, uniquely identified by course_code
    running = True

    while running:
        try:
            option = int(input("""==== Student Management System ====
                            1. Add New Student
                            2. Add New Course
                            3. Enroll Student in Course
                            4. Add Grade for Student
                            5. Display Student Details
                            6. Display Course Details
                            7. Save Data to File
                            8. Load Data from File
                            0. Exit 
                            \nSelect Option: """))

            if option == 0:
                running = False

            elif option == 1:
                Name = input("Enter name of the Student: ")
                Age = int(input("Enter Age of Student: "))
                Address = input("Enter Address of student: ")
                #id=generate_unique_id(input("Enter Student id: ")) This is a hashing feature I added
                id = input("Enter Student id: ")
                student = Student(name=Name, age=Age, address=Address, student_id=id)
                students[id] = student
                print(f'Student {students[id].name} ({id}) got added successfully.')

            elif option == 2:
                Name = input("Enter name of the Course: ")
                Code = input("Enter Course Code: ")
                Instructor = input("Enter name of Instructor: ")
                course = Course(course_name=Name, course_code=Code, instructor=Instructor)
                courses[Code] = course
                print(f'Course {courses[Code].course_name} (Code: {Code}) got added successfully.')

            elif option == 3:
                print("Courses Available: ", [ _.course_code for _ in courses.values()]) #let's show case all the courses
                s_id = input("Enter id of Student you want to add course for: ")
                c_code = input("Enter Course Code: ")
                students[s_id].enroll_course(c_code)
                courses[c_code].add_student(students[s_id])
                print(f'Student {students[s_id].name} enrolled in {c_code}.')

            elif option == 4:
                print("Students Available: ", [_.student_id for _ in students.values()])
                s_id = input("Enter id of Student: ")
                c_code = input("Enter Course Code: ")
                grade = input("Enter Grade: ")
                students[s_id].add_grade(subject=c_code, grade=grade)
                courses[c_code].add_student(students[s_id]) #we also need to add student_id in the Course object for later veiwing course details
                print(f'Grade {grade} added for {students[s_id].name} in {c_code}.')

            elif option == 5:
                s_id = input("Enter Student id: ")
                students[s_id].display_student_info()

            elif option == 6:
                c_code = input("Enter Course code: ")
                courses[c_code].display_course_info()

            elif option == 7:
                filenames = input("Enter file name for Students: ")
                filenamec = input("Enter file name for Courses: ")
                student_list = list(students.values())
                course_list = list(courses.values())
                try:
                    Student.save_students_to_json(student_list, filenames)
                    Course.save_courses_to_json(course_list, filenamec)
                    print("Data saved successfully.")
                except Exception as e:
                    print(f"Error saving data: {e}")

            elif option == 8:
                paths = input("Enter file path for Students: ")
                pathc = input("Enter file path for Courses: ")
                if not os.path.isfile(paths):
                    print(f"Error: {paths} not found.")
                elif not os.path.isfile(pathc):
                    print(f"Error: {pathc} not found.")
                else:
                    try:
                        students = {s.student_id : s for s in Student.load_students_from_json(path=paths)}
                        courses = {c.course_code : c for c in Course.load_courses_from_json(path=pathc)}
                        print("Data loaded successfully.")
                    except Exception as e:
                        print(f"Error loading data: {e}")

        except ValueError:
            print("Invalid input, please enter a number.")
        except KeyError:
            print("Error: Student or Course not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
    print("Goodbye!")
