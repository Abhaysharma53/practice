nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sum = float("-inf")
for i in range(len(nums)):
    curr_sum =0
    for j in range(i, len(nums)):
        curr_sum = curr_sum + nums[j]
        max_sum = max(curr_sum, max_sum)
    
print(max_sum)
