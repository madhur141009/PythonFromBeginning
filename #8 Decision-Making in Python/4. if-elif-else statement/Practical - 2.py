#By if-elif-else statement, input the salary from the user and calculate the tax payable .

s = int(input("Enter your salary : "))
if s <= 50000:
	t = 0.05 * s
elif s <= 60000:
	t = 0.07 * s
elif s <= 70000:
	t = 0.08 * s
else:
	t = 0.10 * s
print("Salary :", s, "Tax :", t)
