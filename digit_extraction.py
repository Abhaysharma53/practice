#extracting the digit of a number
num = 344565

n = num
while n > 0:
    last_digit = n%10
    print(last_digit)
    n = n//10