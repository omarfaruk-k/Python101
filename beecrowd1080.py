li = []
for i in range(100):
    li_input = int(input())
    li.append(li_input)
max_item = max(li)
index_of_max = li.index(max_item)+1
print(max_item)
print(index_of_max)