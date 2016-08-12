'''
Created on Jul 22, 2016

@author: trannh08
'''
# Decimal: 10
# Bit: 1010
# 8's bit  4's bit  2's bit  1's bit
#    1       0       1      0 
#    8   +   0    +  2   +  0  = 10 
print(0b1)      #1
print(0b10)     #2
print(0b11)     #3
print(0b100)    #4
print(bin(1))   #0b1
print(bin(2))   #0b10
print(bin(3))   #0b11
print(bin(4))   #0b100

print(int("1", 2))       #1
print(int("10", 2))      #2
print(int("111", 2))     #7
print(int("0b100", 2))   #4
print(int(bin(5), 2))    #5