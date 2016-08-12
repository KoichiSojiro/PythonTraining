'''
Created on May 11, 2016

@author: trannh08
'''
meal = 44.50
tax = 6.75 / 100
tip = 15.0 / 100

meal = meal + meal * tax
total = meal + meal * tip

print("total: %.3f" % total)

myNumber = 5
div = 5 / 2
multiply = 5 * 2
squareRoot = 5 ** 3
modulo = 5 % 4
print("div: %.3f" % div)
print("multiply: %.0f" % multiply)
print("squareRoot: %.0f" % squareRoot)
print("modulo: %.3f" % modulo)