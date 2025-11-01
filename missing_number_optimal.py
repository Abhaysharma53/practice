nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
n = len(nums)
lst_sum = sum(nums)
range_sum = (n * (n+1))/2
missing_num = int(range_sum - lst_sum)
print(missing_num)