a = [7, 5, -2, 3, 9, 0, 6, 10]
temp = a[-1]
for i in range((len(a)-2),-1, -1):
    a[i+1] = a[i]

a[0] = temp
print(a)