#By if-elif-else statement, accept the percentage of a student and display the grade accordingly.

per = int(input("Enter your percentage : "))
if per >= 85:
	print("A...")
elif per >= 70:
	print("B...")
elif per >= 60:
	print("C...")
elif per >= 45:
	print("D...")
else:
	print("E...")
