'''
Created on May 11, 2016

@author: trannh08
'''
# this import everything from module [math]
# so we have to call [math].[function]
import math
print(math.sqrt(25))

# this import function [sqrt] from module [math]
from math import sqrt
print(sqrt(25))

# this import everything from module [math]
# so we have NO NEED to call [math].[function], just call [function]
from math import *
print(sqrt(25))