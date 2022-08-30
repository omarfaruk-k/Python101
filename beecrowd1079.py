test_case = int(input())
for i in range(test_case):
    num1,num2,num3 = map(float,input().split(" "))
    average = (num1*2+num2*3+num3*5)/10
    print(f"{average:.1f}")