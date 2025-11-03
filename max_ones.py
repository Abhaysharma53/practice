nums = [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1]
lst = list()
i, counter = 0, 0
while i < len(nums):
    if nums[i] ==1:
        counter +=1

    else:
        lst.append(counter)
        counter = 0 

    i+=1
print(max(lst))


