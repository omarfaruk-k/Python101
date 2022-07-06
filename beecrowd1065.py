even_num = 0
for i in range(5):
    number = float(input())
    if number%2 == 0:
        even_num +=1
print(f"{even_num} valores pares")