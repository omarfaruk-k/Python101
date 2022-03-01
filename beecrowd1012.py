A, B, C = [float(x) for x in input().split(' ')]

Tri = (A*C)/2
Circle = 3.14159*C*C
Trapi = (A+B)*C /2
Sq = B*B
Rec = A*B

#print("TRIANGULO: %.3f \nCIRCULO: %.3f \nTRAPEZIO: %.3f \nQUADRADO: %.3f \nRETANGULO: %.3f \n" %(Tri, Circle, Trapi, Sq, Rec), end='\n' )
print("TRIANGULO: %.3f"%Tri)
print("CIRCULO: %.3f"%Circle)
print("TRAPEZIO: %.3f"%Trapi)
print("QUADRADO: %.3f"%Sq)
print("RETANGULO: %.3f"%Rec)