a,b,c =[float (x) for x in input().split(" ")]

if a+b>c and b+c>a and c+a>b:
    p = a+b+c
    print("Perimetro = %.1f"%p)
else:
    a = .5*c*(a+b)
    print("Area = %.1f"%a)
