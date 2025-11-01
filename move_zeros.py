nums = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]
# low,high = 0, len(nums)-1
# while low <=  high:
#     if nums[low] == 0:
#         nums[low], nums[high] = nums[high], nums[low]
#         low += 1
#         high -= 1
#     else:
#         low += 1

temp = []
for i in nums:
    if i != 0:
        temp.append(i)
for i in range(len(temp)):
    nums[i] = temp[i]

for i in range(len(temp), len(nums)):
    nums[i] = 0

print(nums)