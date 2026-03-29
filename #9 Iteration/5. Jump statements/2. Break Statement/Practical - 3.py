#break statement in loop, practical - 3.

for i in ("Hello"):
	if i == "o":
		break
	print(i)
else:
	print("World") #When i = "o", then it will break the for...else loop, so "World" will not be printed.
