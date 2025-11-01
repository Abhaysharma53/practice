a = [1, 1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7, 8, 8, 9]

i, j = 1,0
while i < len(a):
    if a[i] == a[j]:
        i+=1
    else:

        if a[j] != a[i]:
            j+=1
            a[j], a[i] = a[i], a[j]
            i+=1
            

    
print(a, j+1)