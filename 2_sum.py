nums = [5, 9, 1, 2, 4, 15, 6, 3]
target = 13

d = {}
for i in range(len(nums)):
    diff = target - nums[i]
    if diff in d:
        print([d[diff], i])
    else:
        d[nums[i]] = i