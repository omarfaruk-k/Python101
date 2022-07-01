aList = [5, 10, 9, 56, 3, 31, 1, 73, 8, 12]
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if a<10 and b<10:
    print(aList[a:b])
else:
    print("Invalid input")
