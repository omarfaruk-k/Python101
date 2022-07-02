salary = float(input())

if 0<= salary <=400:
    salary2 = salary+ (salary*.15)
    print(f"Novo salario: {salary2:.2f}\nReajuste ganho: {salary*.15:.2f}\nEm percentual: 15 %")
elif 400< salary <=800:
    salary2 = salary+ (salary*.12)
    print(f"Novo salario: {salary2:.2f}\nReajuste ganho: {salary*.12:.2f}\nEm percentual: 12 %")
elif 800< salary <=1200:
    salary2 = salary+ (salary*.1)
    print(f"Novo salario: {salary2:.2f}\nReajuste ganho: {salary*.1:.2f}\nEm percentual: 10 %")
elif 1200< salary <=2000:
    salary2 = salary+ (salary*.07)
    print(f"Novo salario: {salary2:.2f}\nReajuste ganho: {salary*.07:.2f}\nEm percentual: 7 %")
elif salary > 2000:
    salary2 = salary+ (salary*.04)
    print(f"Novo salario: {salary2:.2f}\nReajuste ganho: {salary*.04:.2f}\nEm percentual: 4 %")