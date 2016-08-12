'''
Created on May 11, 2016

@author: trannh08
'''
from pip._vendor.distlib.compat import raw_input
def clinic():
    print ("You've just entered the clinic!")
    print ("Do you take the door on the left or the right?")
    answer = raw_input("Type left or right and hit 'Enter': ").lower().strip()
    if answer == "left" or answer == "l":
        print ("You chose LEFT!")
    elif answer == "right" or answer == "r":
        print ("You chose RIGHT!")
    else:
        print ("You didn't pick left or right! Try again.")
        clinic()
clinic()