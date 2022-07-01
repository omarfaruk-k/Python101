#ID: 0182210012101167

#Question answer - 1
aList = [10, 78, 5, 1, 8, 9, 11]
a = input("Enter anything: ")
b = "    Department of CSE, Lab Final, Spring-2022     "
a = int(a)

print(type(a))

print(b.strip())

print(b.split(","))



#Question answer - 2
newList = [2, 7, 9, 56, 78, 6]
x = 0
end = len(newList)
while x > end:
    if x == 2 or x == 4 or x == 6:
        print("YES")
    else:
        print("NO")
    x =+ 1




#Question answer - 3
listOfNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
if listOfNumber[1] == listOfNumber[10]:
    print("--Got it--")
else:
    print("--Nah!")


#Question answer - 4
a = input("Enter a number: ")
b = input("Enter a number: ")
c = input("Enter a number: ")

if a>b and a>c:
    print(f"{a} is Largest")
elif b>a and b>c:
    print(f"{b} is Largest")
elif c>a and c > b:
    print(f"{c} is Largest")
else:
    print("Two or more number ia equal")