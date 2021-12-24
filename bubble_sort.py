#!/usr/bin/python3

# bubble sorting algorithm

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums = [2,4,1,7,9,5]
sort(nums)
print(nums)
