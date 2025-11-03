nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
curr_sum = 0
max_sum = float("-inf")

for i in nums:
    curr_sum = curr_sum + i
    max_sum = max(curr_sum, max_sum)
    if curr_sum < 0:
        curr_sum =0
    

print(max_sum)