N = int(input())
for i in range(N):
    if i %2 == 0:
        if i>0:
            print("EVEN POSITIVE")
        else:
            print("EVEN NEGATIVE")
    elif i %2 !=0:
        if i > 0:
            print("ODD POSITIVE")
        else:
            print("ODD NEGATIVE")
    else:
        print("NULL")
