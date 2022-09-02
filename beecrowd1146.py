while True:
    x = int(input())
    if x == 0:
        break
    else:
        print(*range(1,x+1))