#break statement in loop, practical - 4.

entry = 0
sum = 0
print("Enter number to sum, negative number ends the list : ")
while True:
	entry = eval(input())
	if entry < 0:
		break
	sum += entry
print("Sum : ", sum)
