marks1 = int(input("Enter marks 1:"))
marks2 = int(input("Enter marks 2:"))
marks3 = int(input("Enter marks 3:"))

#check total percentage
total_percentage = ((marks1 + marks2 + marks3) / 300 )* 100

if total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    print("badhai ho pass ho gaye:", total_percentage, "%")

else:
    print("come on yaar thoda aur mehnat karo:" , total_percentage, )

