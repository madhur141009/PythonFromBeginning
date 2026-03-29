#break statement in loop, practical - 2.

num = 0
for num in range(10):
	num += 1
	if num == 5:
		break
	print("Num has value", str(num))
print("Encountered break!!! Out of loop")
