import sys

if len(sys.argv) == 1:
	print("Usage: python operations.py <number1> <number2>")
	sys.exit(0)

if len(sys.argv) > 3:
	print("input must be 2 integers")
	sys.exit(1)

try:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
except ValueError:
	print("input must be 2 integers")
	sys.exit(1)

s = a + b
diff = a - b
prod = a * b
try:
	quo = a / b
	rem = a % b
except ZeroDivisionError:
	quo = "error: division by zero"
	rem = "error: modulo by zero"

print(f"Sum:         {s}")
print(f"Difference:  {diff}")
print(f"Product:     {prod}")
print(f"Quotient:    {quo}")
print(f"Remainder:   {rem}")

