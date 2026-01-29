"""
Day 4 Activity: Parse nested dictionaries (student database).
Tasks:
1) Get Alice's AI301 grade
2) Calculate Bob's GPA (weighted by credits)
3) Find all students in CS101
4) Get average grade across all courses
5) Find student with highest GPA
"""

students = {
    "S001": {
        "name": "Alice Chen",
        "courses": {
            "CS101": {"grade": 92, "credits": 3},
            "MATH201": {"grade": 88, "credits": 4},
            "AI301": {"grade": 95, "credits": 3},
        },
        "advisor": "Dr. Smith",
    },
    "S002": {
        "name": "Bob Lee",
        "courses": {
            "CS101": {"grade": 85, "credits": 3},
            "MATH201": {"grade": 90, "credits": 4},
        },
        "advisor": "Dr. Patel",
    },
}


#1)
grade1 = students["S001"]["courses"]["AI301"]["grade"]

print(grade1)

#2)
total_points = 0
total_credits = 0

bob_courses = students["S002"]["courses"]

for course in bob_courses.values():
    total_points += course["grade"] * course["credits"]
    total_credits += course["credits"]
bobs_GPA=total_points/total_credits
print(bobs_GPA)


#3)
students_in_CS101 = []

for student in students.values():
    courses = student.get("courses", {})
    if "CS101" in courses:
        students_in_CS101.append(student.get("name"))

print(students_in_CS101)

#5)
highest_GPA = 0
top_student = ""

for student in students.values():
    total_points = 0
    total_credits = 0

    for course in student["courses"].values():
        total_points += course["grade"] * course["credits"]
        total_credits += course["credits"]

    gpa = total_points / total_credits

    if gpa > highest_GPA:
        highest_GPA = gpa
        top_student = student["name"]

print(top_student, highest_GPA) 


# TODO: Implement the tasks above using nested dict access.