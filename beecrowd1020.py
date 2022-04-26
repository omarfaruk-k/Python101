x = int(input())

year = x//365
x %=365
month = x//30
x %=30

print(f"{year} ano(s)\n{month} mes(es)\n{x} dia(s)")