#while loop as infinite loop, practical - 3.
#When the condition for the while loop if always true, then such loops is infinite loop.

a = 1 
while a == 1: #This makes an infinite loop.
	num = int(input("Enter a number : "))
	print("You entered :", num)
print("Goodbye!") #Since, this is an infinite loop this line will never this printed.
