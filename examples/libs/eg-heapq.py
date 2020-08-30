import heapq

#%%
nums = [1, 8, 2, 23, 7, -4, 18, 23, 24, 37, 2]
print(max(nums))
print(min(nums))
# 最大的3个数的索引
print(heapq.nlargest(3,nums))
max_num_index_list = map(nums.index, heapq.nlargest(3, nums))
print(max_num_index_list)
# 最小的3个数的索引
print(heapq.nsmallest(3,nums))
min_num_index_list = map(nums.index, heapq.nsmallest(3, nums))
print(min_num_index_list)

#%%
