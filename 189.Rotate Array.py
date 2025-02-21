#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:58:12 2025

@author: sowmya
"""

class Solution(object):
    
    def rotate(self, nums, k):
        n=len(nums)
        if n==1 or k%n==0:
            print(nums)
            return
        k%=n
        print(k)
        nums.reverse()
        
        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])

        print(nums)
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
""" Aproach 1  
        if (len(nums)==1):
            print(nums)
        else:    
            for i in range ((len(nums)-1),(len(nums)-k-1),-1):
                print(nums[len(nums)-1])
            
                last=nums.pop()
                nums.insert(0,last)
        #print("After rotating for %d,the final list is:%s",%(k,nums))   
                
            print(f"After rotating for {k}, the final list is: {nums}")         
"""
####Aproach 2 ( Reversal - O(n)Time o(1)space )
    #def rotate(self, nums, k):  
             
solution=Solution()   
nums=[1,2,3,4,56,7,78]
k=3     
solution.rotate(nums,k)