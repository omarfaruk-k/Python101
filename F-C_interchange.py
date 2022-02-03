
choice = int(input("Type 1 for fahrenheit to celsius or 2 for celsius to fahrenheit conversion : "))

if choice == 1:
    f = float(input("Enter temperature : "))
    c = 5*(f-32)/9
    print(f"Temperature is {c} degree celsius")

else: 
    c = float(input("Enter temperature : "))
    f = (9*c/5)+32
    print(f"Temperature is {f} degree fahrenheit")

