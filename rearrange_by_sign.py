nums = [5, 10, -3, -1, -10, 6]
pos_list = list()
neg_list = list()
final_list = list()
for i in nums:
    if i > 0:
        pos_list.append(i)
    else:
        neg_list.append(i)
# 
# for j in range(len(nums)//2):
#     final_list.append(pos_list[j])
#     final_list.append(neg_list[j])
for i in range(len(pos_list)):
    nums[i*2] = pos_list[i]
    nums[i*2+1] = neg_list[i]
    
    
    
print(nums)
print(pos_list)
print(neg_list)