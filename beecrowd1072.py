num_of_input = int(input())

inside = 0
outside = 0
for i in range(num_of_input):
    numbers = int(input())
    if 10 <= numbers and numbers <=20:
       inside += 1
    else:
        outside += 1
    i += 1
print(f"{inside} in")
print(f"{outside} out")