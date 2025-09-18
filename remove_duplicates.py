a = [1, 1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7, 8, 8, 9]
dict = {}
def remove_duplicates(lst):
    
    for i in lst:
        dict[i] = 1
   # return list(dict.keys())
    j = 0
    for k in dict:
        lst[j] = k
        j += 1
    return j

res = remove_duplicates(a)
print(res)
