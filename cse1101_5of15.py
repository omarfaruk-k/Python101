#OMAR FARUK KHAN
#ID-0182210012101167

x,y = [int(i) for i in input("Enter two number: ").split(" ")]
reminderX = x%5
reminderY = y%5

if reminderX % 2 == 0 and reminderY % 2 == 0:
    print("Even")
else:
    print("Odd")