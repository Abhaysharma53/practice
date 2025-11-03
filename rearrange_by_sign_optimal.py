nums = [5, 10, -3, -1, -10, 6]
n = len(nums)
pos_index, neg_index = 0, 1
result = [0]*n
for i in nums:
    if i > 0:
        result[pos_index] = i
        pos_index = pos_index +2
    else:
        result[neg_index] = i
        neg_index = neg_index + 2

print(result)