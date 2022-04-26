import math
A,B,C = [float(x) for x in input().split(" ")]

if A==0 or (4*A*C)>B*B:
    print("Impossivel calcular")
else:
    R1 = (-B+(math.sqrt(B*B-4*A*C)))/(2*A)
    R2 = (-B-(math.sqrt(B*B-4*A*C)))/(2*A)
    print("R1 = %.5f" %R1)
    print("R2 = %.5f" %R2)