from random import randrange

def random_number():
	x= (randrange(10))
	return x

def evaluate(a, b):
	if int(a) > int(b):
		print("Too high")
	if int(a) < int(b):
		print("Too low")
	if int(a) == int(b):
		print("Correct")

def playing ():
	tryAgain = False
	while tryAgain == False:
		number = input("Please guess a number between 0-10:\n")
		evaluate(int(number), x)
		if (int(number)==x):
			tryAgain = True

x= int(random_number())

playing()



# print("The random number was: " + str(x))
