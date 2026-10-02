1
N = int(input("Number of students: "))
students = []
courses = []
for i in range(N):
    id = int(input("ID: "))
    name = input("Name: ")
    dob = input("DoB: ")
    s = {
        "id": id,
        "name": name,
        "DoB": dob
    }
    students.append(s)
print(students)
Nc = int(input("\nNumber of courses: "))
for i in range(N):
    print("\nCourse", i + 1)
    id = int(input("Course ID: "))
    name = input("Course name: ")
    c = {
        "id": id,
        "name": name,
        "marks": {}
    }
    courses.append(c)
for course in courses:
        print("\nCourse:", course["name"])
        for student in students:
            mark = float(input(
                "Mark for " + student["name"] + ": "))
            course["marks"][student["id"]] = mark
print("\nStudents ")
for student in students:
    print(student["id"], student["name"], student["DoB"])
print("\nCourses")
for course in courses:
    print(
        course["id"],
        course["name"]
    )
course_id = int(input("\nEnter course ID: "))
for course in courses:
    if course["id"] == course_id:
        print("\nMarks for", course["name"])
        for student in students:
             mark = course["marks"][student["id"]]
             print(
                 student["name"],
                ":",
                mark
            )

             import math
import numpy as np


class Student:

    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.gpa = 0.0


class Course:

    def __init__(self, id, name, credits):
        self.id = id
        self.name = name
        self.credits = credits
        self.marks = {}  # {student_id: mark}



def floor_score(score):
    return math.floor(score * 10) / 10.0



N = int(input("Number of students: "))
students = []
for i in range(N):
    print(f"\nStudent {i + 1}")
    sid = int(input("ID: "))
    name = input("Name: ")
    dob = input("DoB: ")
    students.append(Student(sid, name, dob))


Nc = int(input("\nNumber of courses: "))
courses = []
for i in range(Nc):
    print(f"\nCourse {i + 1}")
    cid = int(input("Course ID: "))
    cname = input("Course name: ")
    credits = int(input("Credits: "))
    courses.append(Course(cid, cname, credits))


for course in courses:
    print(f"\n--- Marks for Course: {course.name} ---")
    for student in students:
        raw_mark = float(input(f"Mark for {student.name}: "))
        course.marks[student.id] = floor_score(raw_mark)


for student in students:
    marks = []
    credits = []
    for course in courses:
        if student.id in course.marks:
            marks.append(course.marks[student.id])
            credits.append(course.credits)

    if credits and sum(credits) > 0:
        marks_arr = np.array(marks)
        credits_arr = np.array(credits)

        # Weighted average formula: sum(mark * credit) / sum(credits)
        weighted_gpa = np.sum(marks_arr * credits_arr) / np.sum(credits_arr)
        student.gpa = floor_score(weighted_gpa)

students.sort(key=lambda s: s.gpa, reverse=True)

print("\n" + "=" * 40)
print("      STUDENT RANKINGS BY GPA")
print("=" * 40)
for rank, s in enumerate(students, 1):
    print(f"Rank {rank} | ID: {s.id} | Name: {s.name} | GPA: {s.gpa:.1f}")