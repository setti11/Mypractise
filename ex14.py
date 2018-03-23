from sys import argv

script, username = argv
prompt = '>> '

print ("Hello %s, welcome to python script %s" % (username, script))

print ('I"d like to ask you a few questions')

print ("Do you like me %s" % (username))
likes = input(prompt)

print ("Where do you live %s" % (username))
place = input(prompt)

print ("What kind of computer you use %s" % (username))
computer = input(prompt)

print ("""
Alright, so you said %r about liking me.
You live in %r. It is very nice place.
And you have a %r computer. Nice.....
""" % (likes, place, computer))

print(f"I like you {username}")