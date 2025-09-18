a = [1, 1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7, 8, 8, 9]
def remove_duplicates(lst):
    n = len(lst)
    if n == 0 or n == 1:
        return n
    i = 0
    j = i+1
    while j < n:
        if lst[i] != lst[j]:
            i+= 1
            lst[i], lst[j] = lst[j], lst[i]
        j+=1
    return i+1

num = remove_duplicates(a)
print(num)