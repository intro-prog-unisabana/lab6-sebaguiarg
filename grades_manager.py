def initialize_dict(student_name, subject_grades):
    student_name = student_name.title()
    return {student_name: subject_grades}


def add_student(student_grades=None):
    if student_grades is None:
        student_grades = {}

    print("Enter student name:")
    name = input().strip().title()

    subjects = {}

    while True:
        print("Enter subject and grade (or 'exit' to finish):")
        entry = input().strip()

        if entry.lower() == "exit":
            break

        subject, grade = entry.split(",")
        subject = subject.strip().title()
        grade = float(grade)

        subjects[subject] = grade

    student_grades[name] = subjects

    print(f"Student {name} successfully added to the grades management system.")
    return student_grades


def get_students(student_grades, keys):
    result = {}

    for name in keys:
        name_title = name.title()

        found = False
        for student in student_grades:
            if student.lower() == name.lower():
                result[student] = student_grades[student]
                found = True
                break

        if not found:
            print(f"{name_title} not found!")

    return result


def avg_by_student(student_grades, keys=None):

    if keys is not None:
        student_grades = get_students(student_grades, keys)

    for student, subjects in student_grades.items():
        avg = sum(subjects.values()) / len(subjects)
        print(f"{student}: {round(avg,1)}")