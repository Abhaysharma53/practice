nums = [55, 32, 97, -55, 45, 32, 85, 21]
largest = float("-inf")
largest_2 = float("inf")

for i in nums:
    if i > largest:
        largest_2 = largest
        largest = i
    else:
        if (i > largest_2) & (i != largest):
            largest_2 = i

print(largest, largest_2)