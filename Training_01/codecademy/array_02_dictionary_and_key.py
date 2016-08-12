'''
Created on May 17, 2016

@author: trannh08
'''
blank_dictionary = {}

residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
print(residents['Puffin'])
print(residents['Sloth'])
print(residents['Burmese Python'])

menu = {}
menu['Chicken Alfredo'] = 14.50
menu['Poops'] = 13
menu['Craps'] = 5
menu['Nothing'] = 2
print(menu['Chicken Alfredo'])
print("There are " + str(len(menu)) + " items on the menu.")
print(menu)

zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
del zoo_animals['Unicorn']
zoo_animals['Rockhopper Penguin'] = 'Crazy Fat Things'
print(zoo_animals)
print(zoo_animals.keys())
print(zoo_animals.items())
