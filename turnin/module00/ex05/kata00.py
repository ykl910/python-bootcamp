kata = (19,42,21)

length = len(kata)
print(f"The {length} numbers are:", end=" ")
for index, value in enumerate(kata):
	if index != length - 1:
		print(f"{value}", end=", ")
	else:
		print(f"{value}")