'''
Created on May 11, 2016

@author: trannh08
'''

my_word = "Hello World!"
fifth_letter = my_word[4]
fifth_letter_to_eigth = my_word[4:8]
fifth_letter_to_end = my_word[4:]
first_letter_to_fifth = my_word[:4]
print (fifth_letter)
print (fifth_letter_to_eigth)
print (fifth_letter_to_end)
print (first_letter_to_fifth)
print (len(my_word))
print (my_word.lower())

pi = 3.14159265359
print("pi number is: " + str(pi))
print(pi)
print("%.2f" % pi)
print("%s" % pi)

string_1 = "Camelot"
string_2 = "place"
print ("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))