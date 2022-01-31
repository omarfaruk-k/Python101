from re import A


marks = int(input("Enter your marks:"))

def grd(grade):
    print(f"You got {grade}")

if marks >= 80:
    grd("A+")
elif marks < 80 and marks >= 70:
    grd("A")
elif marks <70 and marks >= 60:
    grd("B+")
elif marks <60 and marks >= 50:
    grd("B")
else :
    print ("You have failed")
