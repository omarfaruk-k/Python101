money = int(input())
print(money)

for i in [100, 50, 20, 10, 5, 2, 1]:
    print(f"{money//i} nota(s) de R$ {i},00")
    money %=i