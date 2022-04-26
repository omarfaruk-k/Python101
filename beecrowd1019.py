secound = int(input())
hour= secound//3600
secound %= 3600
minute=secound//60
secound %= 60
print(f"{hour}:{minute}:{secound}")