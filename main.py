#Example

abc = 'abcdefghijklmnopqrstuvwxyz'
abc_list = []
count = 1

for i in range(len(abc)):
    abc_list.append(abc[i] * count)
    count += 1
print(abc_list)