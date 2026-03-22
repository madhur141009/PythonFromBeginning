#Python script to input two numbers and find their sum and product

a = eval(input("Enter the first number : ")) #We have not written int() or float() beacuse input can be any. Also we have written eval(), to prevent python treating the input as string
b = eval(input("Enter the second number : "))
c = a + b
print("The sum of", a, "and", b, "is", c)
d = a * b
print("The product of", a, "and", b, "is", d)
