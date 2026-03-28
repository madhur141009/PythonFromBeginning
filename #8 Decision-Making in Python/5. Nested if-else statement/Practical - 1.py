#By if-elif-else statement, tells the inputed number is negative, positive number or zero.

num = int(input("Enter the number : "))
if num >= 0:
	if num == 0:
		print("The number is zero...")
	else:
		print("The number is positive...")
else:
	print("The number is negative...")
