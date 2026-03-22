#Python script to input Distance Covered and Time Taken and find the Speed

d = eval(input("Distance Covered(km) : ")) #We have not written int() or float() beacuse input can be any. Also we have written eval(), to prevent python treating the input as string
t = eval(input("Time Taken(hr) : "))
s = d/t
print("The speed is", s, "(km/hr)")
