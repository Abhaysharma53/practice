a = [1, 2, 5, 6, 7, 9, 10, 3]

def check_aaray(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    return True

res = check_aaray(a)
print(res)