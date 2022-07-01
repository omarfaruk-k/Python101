li = []
li = [float(x) for x in input().split(" ")]
li.sort(reverse=True)

a = li[0]
b = li[1]
c = li[2]

if a >= b+c:
    print("NAO FORMA TRIANGULO")
elif a*a == b*b + c*c:
     print("TRIANGULO RETANGULO")
elif a*a > b*b + c*c:
    print("TRIANGULO OBTUSANGULO")
elif a*a < b*b + c*c:
    print("TRIANGULO ACUTANGULO")


if a == b and b == c:
        print("TRIANGULO EQUILATERO")
elif a == b or b == c:
        print("TRIANGULO ISOSCELES")