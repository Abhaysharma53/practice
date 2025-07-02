#check if 2 numbers are palindrome
num = 13443456
n= num
rev_number = 0
while n > 0:
    last_digit = n%10
    rev_number = rev_number*10 + last_digit
    n = n//10

if num == rev_number:
    print("Palindrome number")
else:
    print("not a palindrome")