h1,m1,h2,m2 = [int (i) for i in input().split(' ')]

if h2 > h1 or (h1==h2 and m1<m2):
    h_diff = h2 - h1
else:
    h_diff = (h2+24) - h1

if m2>m1:
    min_diff = m2 - m1
else:
    min_diff = (m2+60) - m1
    h_diff -= 1


if min_diff == 60:
    h_diff += 1
    min_diff = 0
    

print(f'O JOGO DUROU {h_diff} HORA(S) E {min_diff} MINUTO(S)')