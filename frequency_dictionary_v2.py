lst = [1, 5, 4, 3, 2, 1, 8, 2, 9, 10, 9, 7, 3, 5, 2, 6, 8, 2, 7, 9]
freq_map = dict()
for i in lst:
    freq_map[i] = freq_map.get(i, 0)+1

print(freq_map)