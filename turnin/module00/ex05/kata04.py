kata = (0, 4, 132.42222, 10000, 12345.67)

print(f"module_{kata[0]:02d}", end = ", ")
print(f"ex_{kata[1]:02d}", end = " : ")
print(f"{kata[2]:.2f}", end = ", ")
print(f"{kata[3]:.2e}", end = ", ")
print(f"{kata[4]:.2e}")