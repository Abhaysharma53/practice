#check if a number is armstrong number
num = 1531
n = num
sum = 0
while n> 0:
    last_digit = n%10
    sum += last_digit**3
    n = n//10

if num == sum:
    print("Armstrong number")
    
else:
    print("not a armstrong number")
print(f"Sum = {sum}")

