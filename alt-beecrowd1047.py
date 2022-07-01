h1,m1,h2,m2 = [int (i) for i in input().split(' ')]


startTime = h1+(m1/60)
endTime = h2+(m2/60)

difference = endTime - startTime

hourDiff = int(difference)
minDiff = (difference - int(difference)) * 60

if h1 == h2 and m2 == m1:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    print(f'O JOGO DUROU {hourDiff} HORA(S) E {round(minDiff)} MINUTO(S)')