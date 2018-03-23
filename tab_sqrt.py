import sys
import math
 
script = sys.argv
num = int(sys.argv[1])
sr = int(sys.argv[2])

# num = int(input("Enter any number:"))
# print ("The script is called:", script )

for i in range(1,11):
	print(num,'x',i,'=',num*i)
	
print(f"\nSquareroot of given number {sr} is:", math.sqrt(sr))


