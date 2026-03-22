#Python script to input Principal Amount, Rate of Interest, Time and find the Simple Interest and Amount payable

p = eval(input("Enter the Principal Amount : ")) #We have not written int() or float() beacuse input can be any. Also we have written eval(), to prevent python treating the input as string
r = eval(input("Enter the Rate of Interest : "))
t = eval(input("Enter the Time Taken : "))
si = p*r*t/100
print("Simple Interest is", si)
a = p + si
print("Amount Payable is", a)
