'''
Created on Jul 18, 2016

@author: trannh08
'''
def remove_duplicates(input_list):
    temp_list = []
    for i in input_list:
        if i not in temp_list:
            temp_list.append(i)
    return temp_list

my_list = [1, 1, 2, 3, 2]
my_list = remove_duplicates(my_list)
print(my_list)