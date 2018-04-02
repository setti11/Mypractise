# This script takes file name as input and reads and prints the output on screen

from sys import argv

script, filename = argv
prompt = ">> "
'''
txt = open(filename)

print("Here's your file %r:" % filename)
print (txt.read())
'''

print("Here's your filename again:")
file_again = input(prompt)

txt_again = open(file_again)

print (txt_again.read())
