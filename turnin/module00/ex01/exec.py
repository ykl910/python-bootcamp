import sys

def reverse_swap(str):
	reversed = string[::-1]
	reversed_swaped = reversed.swapcase()
	return reversed_swaped

if len(sys.argv) > 1:
	merged_args = " ".join(sys.argv[1:])
	print(reverse_swap(merged_args))
else:
	print()