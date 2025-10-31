nums = [5, 9, 1, 2, 4, 15, 6, 3]
target = 13
d = dict()
for i in range(len(nums)):
    if target - nums[i] in d:
        print([d[target - i], i])
    else:
        d[nums[i]] = i


   

