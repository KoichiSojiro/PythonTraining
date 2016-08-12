'''
Created on May 12, 2016

@author: trannh08
'''
blank_array = []
numbers = [5, 6, 7, 8]
print ("Adding the numbers at indices 0 and 2...")
print (numbers[0] + numbers[2])

zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
zoo_animals[2] = "hyena"
print (zoo_animals[2])

suitcase = [] 
suitcase.append("sunglasses")
suitcase.append("pantsu")
suitcase.append("laptop")
suitcase.append("pocky")
suitcase.remove("sunglasses")
list_length = len(suitcase) # Set this to the length of suitcase
print ("There are %d items in the suitcase." % (list_length))
print (suitcase)

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
print (animals)
duck_index = animals.index("duck")   # Use index() to find "duck"
print (duck_index)
animals.insert(duck_index, "cobra")
print (animals)