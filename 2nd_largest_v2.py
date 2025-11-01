nums = [55, 32, 97, -55, 45, 32, 85, 21]
largest = float("-inf") 
largest_2 = float("-inf")

for i in nums:
    largest = max(largest, i)

for i in nums:
    if (i > largest_2) & (i != largest):
        largest_2 = i

print(largest_2)
