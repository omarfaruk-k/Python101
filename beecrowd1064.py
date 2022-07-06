pos_num = 0
sum = 0
for i in range(6):
    number = float(input())
    if number > 0:
        pos_num +=1
        sum = sum + number

average = sum / pos_num

print(f"{pos_num} valores positivos" )
print(f"{average:.1f}")