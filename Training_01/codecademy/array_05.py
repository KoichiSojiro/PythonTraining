'''
Created on Jul 12, 2016

@author: trannh08
'''
n = [3, 5, 7]

def print_list(x):
    for i in range(0, len(x)):
        print (x[i])

def print_list2(x):
    for i in x:
        print (i)

print_list(n)
print_list2(n)