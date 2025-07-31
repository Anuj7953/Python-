import random
chars = "abcffhnkggngudjfdfdfgnfnfuurewqwrtyuoplljfazzvn123456788990!@#$%^**"
length = int(input("enter length: "))
password = ""

for a in range(length):
    password += random.choice(chars)

    print("password:" , password)