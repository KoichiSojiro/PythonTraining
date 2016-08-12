'''
Created on Jul 15, 2016

@author: trannh08
'''
choices = ['pizza', 'pasta', 'salad', 'nachos']

print ("Your choices are: ")
for index, item in enumerate(choices):
    print (index, item)

#zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list.
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
for a, b in zip(list_a, list_b):
    if a>b:
        print (a)
    else:
        print (b)

