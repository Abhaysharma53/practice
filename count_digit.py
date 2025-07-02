#count number of digits in a number
num = 4554543545
n = num
counter = 0
while n > 0:
    counter +=1
    n = n//10

print(counter)

