nums = [1, 99, 101, 98, 2, 5, 3, 100, 1, 1]
curr_count = 0
max_count = 0
for i in range(len(nums)):
    curr_count =1
    num = nums[i]
    while num+1 in nums:
        curr_count +=1
        num+=1
    max_count = max(curr_count, max_count)


print(max_count)