'''
Created on May 11, 2016

@author: trannh08
'''
answer = "Left"
if answer == "Left":
    print ("This is the Verbal Abuse Room, you heap of parrot droppings!")

def using_control_once():
    if 1 < 2:
        return "Success #1"
def using_control_again():
    if True == (not not True):
        return "Success #2"
print (using_control_once())
print (using_control_again())

def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
print (greater_less_equal_5(4))
print (greater_less_equal_5(5))
print (greater_less_equal_5(6))

