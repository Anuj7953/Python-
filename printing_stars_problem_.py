'''
for n = 3
  *
 ***
*****
'''

n = int(input("Enter the number:"))

for i in range(1, n + 1):
    # Print leading spaces
    print(' ' * (n - i), end='')
    
    # Print stars
    print('*' * (2 * i - 1))  # 2*i-1 gives the number of stars in each row

    # Move to the next line
    print()  # Prints a newline after each row