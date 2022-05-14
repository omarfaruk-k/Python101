#OMAR FARUK KHAN
#ID-0182210012101167

x,y,z = [int(i) for i in input("Enter three number: ").split(" ")]

if (x>y and x<z) or (x>z and x<y):
    print(f"{x} is the second largest number")
elif (y>x and y<z) or (y<x and y>z):
    print(f"{y} is the second largest number")
elif (z>x and z<y) or (z<x and z>y):
    print(f"{z} is the second largest number")
else:
    print("There is at least two equal number")
