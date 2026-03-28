#for loop, practical - 3, generate the lable of any inputed number.

n = int(input("Enter a number : "))
for i in range(1, 11): #We always add 1 to the second attribute to the range, which tells till which number the loop will be executed
	print(n, "x", i, "=", n*i)	
