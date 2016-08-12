'''
Created on May 11, 2016

@author: trannh08
'''
print (type(42))
print (type(4.2))
print (type('spam'))
print (type(True))


def distance_from_zero(fug):
    if type(fug) == int or type(fug) == float:
        return abs(fug)
    else:
        return "nope"

print (type(-10))
print (distance_from_zero(-10))