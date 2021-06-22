import math
import MovieList
import re   
  
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
class Error(Exception):
    """Base class for other exceptions"""
    pass
class InvalidIC(Error):
	"""Raised when the input value is too small"""
	pass
class invalidEmail(Error):
	"""Raised when the input value is too small"""
	pass
name = str(input("Please enter your name: "))
f = open("Order.txt", "a")
f.write('Name: '+name+'\n')
f.close()
for i in range(0,100):
			while True:
				try:
					ic = str(input("Please enter your IC number: "))
					if len(ic)<12 or len(ic)>12 :
						raise InvalidIC
				except InvalidIC:
					print("Please enter a valid IC Number!")
					continue
				break
			break
f = open("Order.txt", "a")
f.write('IC Number: '+ic+'\n')
f.close()
address = str(input("Please enter your address: "))
phone = str(input("Please enter your phone number: "))
f = open("Order.txt", "a")
f.write('Address: '+address+'\n')
f.write('Phone Number: '+phone+'\n')
f.close()
for i in range(0,100):
			while True:
				try:
					emailAddress = str(input("Please enter your email address: "))
					if(re.search(regex,emailAddress)):
						break
					else:
						raise invalidEmail
				except invalidEmail:
					print("Please enter a valid email address!")
					continue
				break
			break
f = open("Order.txt", "a")
f.write('Email Address: '+emailAddress+'\n')
f.close()
for i in range(0,100):
			while True:
				try:
					ticketQuantity = int(input("Ticket quantity: "))
				except:
					print("Please enter numbers only!")
					continue
				break
			break
f = open("Order.txt", "a")
ticketQuantityToString = str(ticketQuantity)
f.write('Ticket Quantity: '+ticketQuantityToString+'\n')
f.close()

  

print("Welcome to Movie Booking System",name,"!")
MovieList.movieList()
for i in range(0,100):
			while True:
				try:
					print("Enter the movie number only.")
					movie = int(input("Please choose the movie: "))
				except:
					print("Please enter numbers only!")
					continue
				break
			break


for i in range(0,100):
			while True:
				try:
					print("Enter the snack number only.")
					snack = int(input("Please choose the snack: "))
				except:
					print("Please enter numbers only!")
					continue
				break
			break
if movie == 1:
	totalPrice = ticketQuantity*17
	totalToString = str(totalPrice)
	movieName = "Godzilla Vs. Kong"
	if snack == 1:
		snackName = "Coca Cola + Popcorn"
	elif snack == 2:
		snackName = "Pepsi + Popcorn"
	elif snack == 3:
		snackName = "Hot Chocolate + Popcorn"
	elif snack == 4:
		snackName = "Hot Coffee + Popcorn"
	f = open("Order.txt", "a")
	f.write('Movies: '+movieName+'\n')
	f.write('Snacks: '+snackName+'\n')
	print("Name: ",name)
	print("IC Number: ",ic)
	print("Address: ",address)
	print("Telephone Number: ",phone)
	print("Email Address: ",emailAddress)
	print("Ticket Quantity: ",ticketQuantity)
	print("Movie Name: ",movieName)
	print("Snacks: ",snackName)
	print("The total payment is:RM",totalToString)
elif movie == 2:
	totalPrice = ticketQuantity*18
	totalToString = str(totalPrice)
	movieName = "Mortal Kombat"
	if snack == 1:
		snackName = "Coca Cola + Popcorn"
	elif snack == 2:
		snackName = "Pepsi + Popcorn"
	elif snack == 3:
		snackName = "Hot Chocolate + Popcorn"
	elif snack == 4:
		snackName = "Hot Coffee + Popcorn"
	f = open("Order.txt", "a")
	f.write('Movies: '+movieName+'\n')
	f.write('Snacks: '+snackName+'\n')
	print("Name: ",name)
	print("IC Number: ",ic)
	print("Address: ",address)
	print("Telephone Number: ",phone)
	print("Email Address: ",emailAddress)
	print("Ticket Quantity: ",ticketQuantity)
	print("Movie Name: ",movieName)
	print("Snacks: ",snackName)
	print("The total payment is:RM",totalToString)
elif movie == 3:
	totalPrice = ticketQuantity*20
	totalToString = str(totalPrice)
	movieName = "Fast and Furious 9"
	if snack == 1:
		snackName = "Coca Cola + Popcorn"
	elif snack == 2:
		snackName = "Pepsi + Popcorn"
	elif snack == 3:
		snackName = "Hot Chocolate + Popcorn"
	elif snack == 4:
		snackName = "Hot Coffee + Popcorn"
	f = open("Order.txt", "a")
	f.write('Movies: '+movieName+'\n')
	f.write('Snacks: '+snackName+'\n')
	print("Name: ",name)
	print("IC Number: ",ic)
	print("Address: ",address)
	print("Telephone Number: ",phone)
	print("Email Address: ",emailAddress)
	print("Ticket Quantity: ",ticketQuantity)
	print("Movie Name: ",movieName)
	print("Snacks: ",snackName)
	print("The total payment is:RM",totalToString)
elif movie == 4:
	totalPrice = ticketQuantity*20
	totalToString = str(totalPrice)
	movieName = "Black Widow"
	if snack == 1:
		snackName = "Coca Cola + Popcorn"
	elif snack == 2:
		snackName = "Pepsi + Popcorn"
	elif snack == 3:
		snackName = "Hot Chocolate + Popcorn"
	elif snack == 4:
		snackName = "Hot Coffee + Popcorn"
	f = open("Order.txt", "a")
	f.write('Movies: '+movieName+'\n')
	f.write('Snacks: '+snackName+'\n')
	print("Name: ",name)
	print("IC Number: ",ic)
	print("Address: ",address)
	print("Telephone Number: ",phone)
	print("Email Address: ",emailAddress)
	print("Ticket Quantity: ",ticketQuantity)
	print("Movie Name: ",movieName)
	print("Snacks: ",snackName)
	print("The total payment is:RM",totalToString)