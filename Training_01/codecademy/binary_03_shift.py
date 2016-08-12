'''
Created on Jul 22, 2016

@author: trannh08
'''
number = 0b10       #2
print(number)
print(number << 1)  #4 = number**(1+1)
print(number << 2)  #8 = number**(1+2)
print(number << 3)  #16 = number**(1+3)

number = 0b10000    #16
print(number)
print(number << 1)  #32 = number**(1+1)
print(number << 2)  #64 = number**(1+1)
print(number << 3)  #128 = number**(1+1)
print(number >> 1)  #8 = sqrt(number, 1+1)
print(number >> 2)  #4 = sqrt(number, 1+2)
print(number >> 3)  #2 = sqrt(number, 1+3)