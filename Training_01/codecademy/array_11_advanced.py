'''
Created on Jul 19, 2016

@author: trannh08
'''
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print(evens_to_50)

even_squares = [x**2 for x in evens_to_50]
print(even_squares)

my_slice = [i for i in range(1, 20)]
print(my_slice[3:14:2])
print(my_slice[::2])
print(my_slice[:5:])
print(my_slice[4::])
print(my_slice[::-2])


