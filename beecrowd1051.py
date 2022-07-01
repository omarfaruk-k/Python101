salary = float(input())
if salary <= 2000.00:
    print("Isento")
elif salary <= 3000.00:
    taxable_salary = salary - 2000.00
    tax = taxable_salary * 0.08
    print(f"R$ {tax:0.2f}")
elif salary <= 4500.00:
    taxable_salary = salary - 3000.00
    tax = (taxable_salary * 0.18) + 80
    print(f"R$ {tax:0.2f}")
elif salary > 4500.00:
    taxable_salary = salary - 4500.00
    tax = (taxable_salary * 0.28) + 80 + 270
    print(f"R$ {tax:0.2f}")