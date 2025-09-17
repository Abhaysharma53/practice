s = "dzyaxyyzaaaa"
q = ['d', 'a', 'y', 'x', 't']

d = {}
for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
for i in q:

    if i in d:
        print(d[i])
    else:
        print(0)

