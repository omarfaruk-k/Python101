end = int(input())
start = int(input())
summ = 0
for i in range(start+1,end):
        if i %2 != 0:
            summ += i
print(summ)
