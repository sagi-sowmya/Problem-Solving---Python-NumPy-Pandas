#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:57:12 2025

@author: sowmya
"""

class Solution(object):
    def majorityElement(self, nums):
        k=0
        for i in range(len(nums)):
            if k==0:
                output=nums[i]
                k+=1
            elif k>0 and (nums[i]==output):
                output=nums[i]
                k+=1
            else:
                k-=1

        return output                 
        
        
        """
        :type nums: List[int]
        :rtype: int
        
        n=len(nums)
        k=1
        if (1<=n<=5*(10**4)):
            for i in range(0,n-1):
                if((-10**9)<=nums[i]<=(10**9)):
                    if k==0:
                        k+=1 if nums[i]==nums[i+1] else k-=1 
                        """


                    

solution=Solution()
nums=[2,2,1,1,1,2,2,3]

print("Most occurred element:",solution.majorityElement(nums))        