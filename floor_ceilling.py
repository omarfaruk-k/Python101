import math
choice_for_floor = input("Do you want to check floor? \n ----Type YES or NO: ")
choice_for_ceilling = input("Do you want to check ceilling? \n ----Type YES or NO: ")

if choice_for_ceilling =="YES" or choice_for_floor == "YES":
    number = float(input("Enter the number: "))

    if choice_for_floor == "YES":
        print(f"The floor is: {math.floor(number)}")
    if choice_for_ceilling == "YES":
        print(f"The ceilling is: {math.ceil(number)}")


elif choice_for_ceilling =="NO" or choice_for_floor == "NO":
    print("----------You choose nothing----------")
else:
    print("----------invalid input----------")