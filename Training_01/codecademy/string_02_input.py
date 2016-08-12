'''
Created on May 11, 2016

@author: trannh08
'''
from pip._vendor.distlib.compat import raw_input
name = raw_input("name? ")
age = int(raw_input("age? "), 10)

print ("Ah, so your name is %s, " \
"your age is %i." % (name, age))
print ("Ah, so your name is " + name + 
       ", your age is " + str(age) + ".")