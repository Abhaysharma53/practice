nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
n = len(nums)

d = dict()
for i in range(n+1):
    d[i]=0

for i in nums:
    if i in d:
        d[i] = 1
#print(d)
for k,v in d.items():
    if v == 0:
        print(k)
