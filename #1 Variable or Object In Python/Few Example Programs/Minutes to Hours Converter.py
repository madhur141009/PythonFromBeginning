#Python script to input minutes and covert them in hours and minutes

t = int(input("Enter the time in minutes : "))
h = t//60
m = t%60 #% tells the remainder when divided
print("Hours are", h)
print("Minutes are", m)
