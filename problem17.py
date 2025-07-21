marks = int(input("Enter your marks:"))

if marks <100 and marks >90:
    print("Excellent")

elif marks <90 and marks>80:
    print("Grade A")
    
elif marks <80 and marks >70:
    print("Grade B")

else :
    print("failed , come next year")