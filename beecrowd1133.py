a = int(input())
b = int(input())
x=min(a,b)
y=max(a,b)
for i in range(x,y):
    if i%5 == 2 or i%5==3:
        print(i)
