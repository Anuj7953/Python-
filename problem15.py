p1 = "make a lot of money"
p2 = "buy now"

message = input("Enter your comment")

if (p1 in message)or (p2 in message):

    print("its a spam:", p1)
else:
    print("its not a spam")