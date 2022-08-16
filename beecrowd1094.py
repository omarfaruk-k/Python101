test_case = int(input())
total_number = 0
total_C = 0
total_R = 0
total_S = 0
for i in range(test_case):
    number,animal = input().split(" ")
    number = int(number)
    if animal =='C':
        total_C += number
    elif animal =='R':
        total_R += number
    elif animal =='S':
        total_S += number

    total_number += number

print(f"Total: {total_number} cobaias")
print(f"Total de coelhos: {total_C}")
print(f"Total de ratos: {total_R}")
print(F"Total de sapos: {total_S}")

print(f"Percentual de coelhos: {(total_C/total_number)*100:.2f} %")
print(f"Percentual de ratos: {(total_R/total_number)*100:.2f} %")
print(f"Percentual de sapos: {(total_S/total_number)*100:.2f} %")