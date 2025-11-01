nums1 = [1, 1, 1, 2, 4, 6, 7]
nums2 = [1, 2, 3, 6 ,7 ,8, 9, 10]

m = len(nums1)
n = len(nums2)
result = list()
i =0
j= 0
while i < m and j< n:
    if nums1[i] <= nums2[j]:
        if len(result) == 0 or result[-1] != nums1[i]:
            result.append(nums1[i])
        i+=1
    else:
        if nums2[j] <= nums1[i]:
            if len(result) == 0 or result[-1] != nums2[j]:
                result.append(nums2[j])
            j+=1

while i < m:
    if result[-1] != nums1[i]:
        result.append(nums1[i])
    i+=1

while j < n:
    if result[-1] != nums2[j]:
        result.append(nums2[j])
    j+=1

print(result)

