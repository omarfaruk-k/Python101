
#from pickle import FALSE, TRUE


def check(num):
    if num % 2 == 0:
        return True
    else:
        return False

EVEN = []
start = 0
limit = int(input("Enter limit:"))
while start <= limit:
     if check (start):
         EVEN.append(start)
     start = start + 1

print(f"Even numbers are {EVEN}")



