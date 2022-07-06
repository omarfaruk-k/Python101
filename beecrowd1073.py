last = int(input())
i = 1
while i <= last:
    if i%2 == 0:
        print(f"{i}^2 = {pow(i,2)}")
    i += 1