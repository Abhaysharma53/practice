n = [1, 3, 2, 5, 7, 8, 2, 6, 2, 3, 8, 5, 7, 9, 5, 3, 1, 8, 4, 8, 4, 2]
m = [10, 111, 1, 9, 5, 67, 2]

hash_list = [0] * 11
for i in n:
    hash_list[i] += 1

print(hash_list)

for j in m:
    if (j < 0) or (j> 10):
        print("0")
    else:
        print(hash_list[j])
