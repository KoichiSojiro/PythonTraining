'''
Created on May 11, 2016

@author: trannh08
'''
bool_one = (2**3 == 108 % 100 or "Cleese" == "King Arthur")
bool_two = (True or False)
bool_three = (100**0.5 >= 50 or False)
bool_four = (True or True)
bool_five = (1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1)

bool_one = False
bool_two = (-(-(-(-2))) == -2 and 4 >= 16**0.5)
bool_three = (19 % 4 != 300 / 10 / 10 and False)
bool_four = (-(1**2) < 2**0 and 10 % 10 <= 20 - 10 * 2)
bool_five = True and True

bool_one = (not True)
bool_two = (not 3**4 < 4**3)
bool_three = (not 10 % 3 <= 10 % 2)
bool_four = (not 3**2 + 4**2 != 5**2)
bool_five = (not not False)