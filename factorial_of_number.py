# 5! = 1 * 2 * 3 * 4 * 5

n = int(input("Enter  the number: "))

product = 1

for i in range(1, n+1):  # if range is (1, n) it goes till n-1 , so n+1 is taken
	product = product * i
	
print(f"The factorial of {n} is {product}")