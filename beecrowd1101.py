while True:
    m,n = map(int,input().split())
    x = max(m,n)
    y = min(m,n)
    sum = 0

    if m <= 0 or n <= 0:
        break
    else:
        for i in range(y,x+1):
            print(i,end=" ")

            sum += i
        print(f"Sum={sum}")