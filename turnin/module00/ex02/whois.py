import sys

if len(sys.argv) != 2:
	print("more than one argument is provided")
else:
	try:
		number = int(sys.argv[1])
		if number == 0:
			print("I'm Zero.")
		elif number % 2 == 1:
			print("I'm Odd.")
		else:
			print("I'm Even.")
	except ValueError:
		print("argument is not an integer")