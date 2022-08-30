password = 2002

while True:
    inputed = int(input())
    if password == inputed:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")