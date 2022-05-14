#OMAR FARUK KHAN
#ID-0182210012101167

x,y = [int(i) for i in input("Enter two number: ").split(" ")]

avg = (x+y)/2

if x > avg:
    print(f"{x} is greater than the average of the two numbers")
elif y > avg:
    print(f"{y} is greater than the average of the two numbers")