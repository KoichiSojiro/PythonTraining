'''
Created on Jul 11, 2016

@author: trannh08
'''
from src.calculation_01 import total

lloyd = {
    "name": "Lloyd",
    "homework": [],
    "quizzes": [],
    "tests": []
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

lloyd["homework"] = [90.0, 97.0, 75.0, 92.0]
lloyd["quizzes"] = [88.0, 40.0, 94.0]
lloyd["tests"] = [75.0, 90.0]

students = [lloyd, alice, tyler]
#print(students)

for student in students:
    print(student["name"])
    print(student["homework"])
    print(student["quizzes"])
    print(student["tests"])

def average(numbers):
    #for number in numbers:
    total = sum(numbers)
    result = float(total) / len(numbers)
    return result

def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return homework * 10/100 + quizzes * 30/100 + tests * 60/100

def get_letter_grade(result):
    if result >= 90:
        return "A"
    elif result >= 80:
        return "B"
    elif result >= 70:
        return "C"
    elif result >= 60:
        return "D"
    else:
        return "F"

def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)
    

#print(get_average(students[1]))
print(get_class_average(students))
print("class average: " + str(get_class_average(students)))