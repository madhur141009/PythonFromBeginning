#By if-else statement, calculates the money earned in a week and display an appropriate message.

hourlypay = int(input("Your earning per hour : "))
hoursperweek = int(input("How many hours a week do you work? "))
weeklypay = hourlypay * hoursperweek
if weeklypay > 400:
	print("You are afford to live alone.")
else: 
	print("You can't afford to live alone.")
