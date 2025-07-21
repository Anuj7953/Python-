name = {"dog": "kutta",
        "cat": "billi"}

word = input("enter the word you want the meaning of:")

if word in name:
    print(name[word])
else:
    print("Word not found in dictionary.")