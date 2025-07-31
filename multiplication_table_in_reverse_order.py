# Program to print multiplication table of a number in reverse order

# Input from user
n = int(input("Enter the number to print its multiplication table in reverse order: "))

# Loop from 10 to 1 (reverse)
for i in range(10, 0, -1):
    print(f"{n} x {i} = {n * i}")
