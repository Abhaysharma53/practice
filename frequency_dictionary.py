lst = [1, 5, 4, 3, 2, 1, 8, 2, 9, 10, 9, 7, 3, 5, 2, 6, 8, 2, 7, 9]
freq_map = dict()
for i in lst:
    if i in freq_map:
        freq_map[i] += 1
    else:
        freq_map[i] = 1

x = 5
#print(freq_map[x])
print(freq_map.keys())
print(freq_map.values())