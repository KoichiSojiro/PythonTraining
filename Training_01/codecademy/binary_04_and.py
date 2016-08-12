'''
Created on Jul 22, 2016

@author: trannh08
'''
#    a:    00101010    42
#    b:    00001111    15       
#=========================
#a & b:    00001010    10

# result = 0 if contain 0
# 1 & 1 = 1
# 0 & 0 = 0
# 0 & 1 = 0

a = 0b101010
b = 0b1111
print(a&b)