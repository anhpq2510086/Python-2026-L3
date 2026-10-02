def input_students():
    students = []

    n = int(input("Number of students: "))

    for i in range(n):
        print(f"\nStudent {i + 1}")

        id = int(input("ID: "))
        name = input("Name: ")
        dob = input("DoB: ")

        students.append(Student(id, name, dob))

    return students


def input_courses():
    courses = []

    nc = int(input("\nNumber of courses: "))

    for i in range(nc):
        print(f"\nCourse {i + 1}")

        id = int(input("Course ID: "))
        name = input("Course name: ")

        courses.append(Course(id, name))

    return courses


def input_marks(students, courses):
    for course in courses:
        print(f"\nCourse: {course.name}")

        for student in students:
            mark = float(
                input(f"Mark for {student.name}: ")
            )

            course.marks[student.id] = mark