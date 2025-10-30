#coding question - interview
# given a series , find the element with highest frequency, if there is a clash return the max out of it
lst = [1, 2, 7, 1, 6, 3, 1, 2, 1, 4, 5, 2, 2]
l = list()
d = dict()
for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

max_freq = max(d.values())
print(d)
print(max_freq)
for key, value in d.items():
    if value == max_freq:
        l.append(key)
print(max(l))

     
