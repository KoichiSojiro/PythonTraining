'''
Created on Jul 22, 2016

@author: trannh08
'''
def check_bit4(num):
    mask = 0b1000
    result = num & mask
    if result > 0:
        print("Bit #04 was on.")
    else:
        print("Bit #04 was off.")
    return

check_bit4(1)   #1 = 1        off
check_bit4(10)  #10 = 1010    on
check_bit4(18)  #10 = 10010   off