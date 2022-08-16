N = int(input())
for i in range(N):
    number = int(input())
    if number > 0:
        if number % 2 == 0:
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    elif number < 0:
        if number %2 ==0:
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")
    elif number ==0:
        print("NULL")
