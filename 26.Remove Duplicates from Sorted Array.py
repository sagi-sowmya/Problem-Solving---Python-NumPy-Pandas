#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:54:32 2025

@author: sowmya
"""

class Solution(object):
    def removeDuplicates(self, nums):
        k=0
        
        for i in range(0,len(nums)-1):
            if (nums[i]!=nums[i+1]):
                nums[k]=nums[i]    
                k+=1
                
        nums[k]=nums[len(nums)-1]
        k+=1
        for i in range(k,len(nums)):
            nums[i]='_'
        print ("length of nums",k)
        print(nums) 
        return k 

solution = Solution()
nums=[0,0,1,1,4,4,5,5,6,7,7,7,7]

if (1 <= len(nums) <= 10**4 and all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) and all(-100 <= nums[i] <= 100 for i in range(len(nums)))):
    solution.removeDuplicates(nums)
    #print(f"Updated list: {nums}")
else:
    print("Constraints not satisfied")
