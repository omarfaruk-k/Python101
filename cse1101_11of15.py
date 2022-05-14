#OMAR FARUK KHAN
#ID-0182210012101167
a = int(input("Enter the marks: "))
if 100<a or a<0:
    print("This is not marks")
elif a>=80:
    print("A+")
elif a>=70:
    print("A")
elif a>=60:
    print("A-")
elif a>=50:
    print("B")
elif a>=40:
    print("C")
elif a>=33:
    print("D")
elif a<33:
    print("F")