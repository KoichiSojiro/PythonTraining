'''
Created on Jul 27, 2016

@author: trannh08
'''
with open("C:\\Users\\trannh08\\Downloads\\output.txt", "r") as textfile:
    print(textfile.read())

# with ... as ...
# is the same with using() in C#
# we have no need to close the stream