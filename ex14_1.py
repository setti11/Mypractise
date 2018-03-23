from sys import argv

script, username = argv
prompt = '>>> '

print ("Hi %s, I'm the %s script" % (username, script))

print ("Hi %s, How are you doing today" % (username))
doing = input(prompt)

print("Where do you live %s" %(username))
live = input(prompt)



print ("So your name is {0}".format(username))
print ("{0} is {1} today".format(username, doing))
print ("{0} lives in {1}, it is very nice place".format(username, live))