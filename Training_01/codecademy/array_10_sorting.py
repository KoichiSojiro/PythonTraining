'''
Created on Jul 18, 2016

@author: trannh08
'''
from _operator import itemgetter

my_list = [6,8,12,2,23]
my_list = sorted(my_list, reverse=False)
print(my_list)

my_list = sorted(my_list, reverse=True)
print(my_list)

my_list.sort(key=None, reverse=False)
print(my_list)

colors = ["blue", "lavender", "red", "yellow"]
colors = sorted(colors, key=lambda color: len(color), reverse=True)
print(colors)

furniture = {"table": 1, "chair": 2, "desk": 4}
furniture = sorted(furniture.keys())
print(furniture)

student_tuples = [
                  ('john', 'A', 15),
                  ('jane', 'B', 12),
                  ('dave', 'B', 10),
                  ]
student_tuples = sorted(student_tuples, key=lambda student: student[0], reverse=False)
print(student_tuples)
student_tuples = sorted(student_tuples, key=lambda student: student[1], reverse=False)
print(student_tuples)
student_tuples = sorted(student_tuples, key=lambda student: student[2], reverse=False)
print(student_tuples)
#below technique is the same
student_tuples = sorted(student_tuples, key=itemgetter(0), reverse=False)
print(student_tuples)
student_tuples = sorted(student_tuples, key=itemgetter(1), reverse=False)
print(student_tuples)
student_tuples = sorted(student_tuples, key=itemgetter(2), reverse=False)
print(student_tuples)