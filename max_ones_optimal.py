nums = [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1]
n = len(nums)
curr_count = 0
maxi_count = 0
i = 0
while i < len(nums):
    if nums[i] != 0:
        curr_count += 1
    else:
        if curr_count > maxi_count:
            maxi_count = curr_count
        curr_count = 0
    i+=1

if curr_count > maxi_count:
    maxi_count = curr_count
print(maxi_count)
