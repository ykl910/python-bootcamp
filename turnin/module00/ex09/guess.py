import random

print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!\n""")
number = random.randint(1, 99)
attempts = 1
while True:
	user_number = input("What's your guess between 1 and 99?\n")
	if user_number.lower() == "exit":
		print("Goodbye!")
		break
	if (number == 42 and user_number == "42"):
		print("The answer to the ultimate question of life, the universe and everything is 42.")
		print(f"Congratulations! You won in {attempts} attempts!")
		break
	try:
		user_number = int(user_number)
	except:
		print("not a valid number")
		attempts += 1
		continue
	if (user_number < number):
		print("Too low")
		attempts += 1
	elif (user_number > number):
		print("Too high")
		attempts += 1
	else:
		print("Congratulations, you've got it")
		print(f"You won in {attempts} attempts!")
		break