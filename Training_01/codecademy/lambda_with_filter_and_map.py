'''
Created on Jul 21, 2016

@author: trannh08
'''
languages = ["HTML", "JavaScript", "Python", "Ruby"]
languages_filtered = filter(lambda y: y=="Python", languages)
print (languages_filtered)
for i in languages_filtered:
    print(i)

# map() and filter() works similar to each other while:
# map() returns Booleans list with [True/False]
# filter() returns Values list with that match condition only
squares = [x**2 for x in range(1, 11)]
squares_filtered = filter(lambda x: x >= 30 and x <= 70, squares)
squares_mapped = map(lambda x: x >= 30 and x <= 70, squares)
print(squares_filtered)
for i in squares_filtered:
    print(i)
for i in squares_mapped:
    print(i)

