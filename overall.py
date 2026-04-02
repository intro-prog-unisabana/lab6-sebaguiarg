my_dict = {"s1": {"hw1": 80, "hw2": 90, "hw3": 100},
  "s2": {"hw1": 70, "hw2": 75, "hw3": 85},
  "s3": {"hw1": 95, "hw2": 85, "hw3": 90}}


def student_averages(my_dict):
    if not my_dict:
        return {}
    
    averages = {}
    for student, assignments in my_dict.items():
        total = sum(assignments.values())
        count = (len(assignments))
        averages[student] = round(total/count)
    return averages


def assignment_averages(my_dict):
    if not my_dict:
        return {}
    

    student = list(my_dict.values())[0]
    tarea = student.keys()

    task_average = {}

    for task in tarea:
        all_grades = []
        for assigments in my_dict.values():
            all_grades.append(assigments[task])

        average = sum(all_grades)/len(all_grades)
        task_average[task] = round(average)
    
    return task_average

print(student_averages(my_dict))
print(assignment_averages(my_dict))