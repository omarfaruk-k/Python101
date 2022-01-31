choice = input("Type EVEN for even numbers, ODD for odd numbers: ")
if choice == "EVEN":
    limit1 = int(input("Enter limit: "))
    for i in range(0,limit1+1, 2):
        print(i, end="  ")

elif choice == "ODD":
    limit2 = int(input("Enter limit: "))
    for i in range(0,limit2+1, 1):
        if i%2 == 0:
            continue
        print(i, end="  ")








