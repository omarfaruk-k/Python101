a,b,c,d = [float (x) for x in input().split(" ")]

average = (a*2+b*3+c*4+d*1)/10
print(f"Media: {average:.1f}")
if average >= 7:
    print("Aluno aprovado.")
elif average <5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    e = float(input())
    print(f"Nota do exame: {e:.1f}")
    average2 = (average+e)/2


    if average2 >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {average2:.1f}")
