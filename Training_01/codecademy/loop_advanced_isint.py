'''
Created on Jul 15, 2016

@author: trannh08
'''
def is_int(x):
    my_array = []
    my_array2 = []
    index = 0
    floating_point = 0
    for char in str(x):
        my_array.append(char)
    for instance in my_array:
        if instance == ".":
            index = floating_point
            break
        else:
            floating_point += 1
    if index > 0:
        for c in range(index+1,len(my_array)):
            my_array2.append(my_array[c])
        for c in my_array2:
            if int(c)>0:
                return False
    return True
print(is_int(-4.0))