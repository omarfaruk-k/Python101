money = float(input())
print("NOTAS:")

for i in [100, 50, 20, 10, 5, 2]:
    print(f"{money//i} nota(s) de R$ {i},00")
    money %=i

print("MOEDAS:")
for i in [1, 0.50, 0.25, 0.10, 0.05, 0.01]:
    print(f"{money//i} meoda(s) de R$ {i},00")
    money %=i