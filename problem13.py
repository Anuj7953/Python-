a1 = int(input("Enter the number 1: "))
a2 = int(input("Enter the number 2: "))
a3 = int(input("Enter the number 3: "))

if a1>a2 and a1>a3:
    print("number is greater:", a1)

elif a2>a1 and a2>a3:
    print("number is greater:", a2)

else:
    print("number is greater:", a3)