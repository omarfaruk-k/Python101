a,b = [int(i) for i in input().split(' ')]

if b>a:
    print(f'O JOGO DUROU {b-a} HORA(S)')
else:
    print(f'O JOGO DUROU {(b+24)-a} HORA(S)')