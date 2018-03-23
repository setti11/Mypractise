# This is for formatter

formatter = "%r %r %r %r"
instr = '%s', '%s', '%d', '%s', '%s', '%s', '%s'
print (instr)

print (formatter % (1,2,3,4))
print (formatter % ("one","Two","three","Four"))
print (formatter % (True, False, True, False))
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % (
    "I had this thing",
    "That you could type right up ",
    "But it didn't sing",
    "So, I say Good Bye."
    ))



#formatter = "%r %r %r %r"

#print (formatter % (1,2,3,4))
##print (formatter % ("one", "Two", "Three", "four"))
#print (formatter % (True, False, True, False))
#print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % (
    "I had this thing",
    "So, I say Good Bye.",
    "Hello,",
    "It's okay"
    ))
