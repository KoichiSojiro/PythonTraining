'''
Created on May 17, 2016

@author: trannh08
'''
start_list = [5, 3, 1, 2, 4]
for number in start_list:
    print("each number of start_list: " + str(number))

start_list.sort()
print("sorted start_list: " + str(start_list))

webster = {
    "Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}
for index in webster:
    print (index)
    print (webster[index])
