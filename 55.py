#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:05:57 2025

@author: sowmya
"""

import numpy as np
class Solution:
    def canJump(self, nums) -> bool:
        i=0
        nums=np.atleast_1d(nums)
        zero_indices= np.where(nums==0)[0]
        print("Zero indices are:",zero_indices)
        #while (0 in nums[:len(nums)-2]):
        if zero_indices!=0:
            for i in zero_indices:
                
            

        while (i<(len(nums)-1) and nums[i]!=0):
            i+=nums[i]
        return True if (i==len(nums)-1)  else False  



solution=Solution()
nums=[2,3,0,1,2,0,4]
print("Result=",solution.canJump(nums))        


"""Incomplete
"""