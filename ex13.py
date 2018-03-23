from sys import argv

script, first, second, third = argv

print ("The script is called:", script)
print ("The first argument you have passed is", first)
print ("The second argument you have passed is", second)
print ("Third argument you have passed is", third)



'''
import sys
print ("number of arguments", len(sys.argv))
print ("arguments list you have passed", str(sys.argv))
age  = (sys.argv[1])
height = str(sys.argv[2])
weight = (sys.argv[3])

print(f"You are age is {age} and height is {height} feet with weight {weight} kgs")

'''

''' # It is used to print tables for the number given
import sys

num = int(sys.argv[1])

for i in range(1,11):
	print(num,'x',i,'=',num*i)
	
'''

''' 
# Prints Table for the given number and squareroot of number
import sys, math

num = int(sys.argv[1])

for i in range(1,11):
	print(num,'x',i,'=',num*i)
	
sr = int(sys.argv[2])
print(f'The squareroot of given number {sr} is', math.sqrt())