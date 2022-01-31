marks = int(input("Enter your marks:"))

if marks >= 80:
    print("You got A+")
elif marks < 80 and marks >= 70:
    print("You got A")
elif marks <70 and marks >= 60:
    print("You got B+")
elif marks <60 and marks >= 50:
    print("You got B")
else :
    print ("You have failed")
