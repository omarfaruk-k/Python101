case = int(input())
count = 0
for i in range(case):
    m,n = map(int,input().split())
    x = min(m,n)
    y = max(m,n)
    for j in range(x+1,y):
        if j%2 != 0:
             count +=j
    print(count)
    count = 0