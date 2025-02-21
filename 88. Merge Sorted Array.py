#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:49:55 2025

@author: sowmya
"""

class Solution:
    def merge(self,nums1,m,nums2,n):
        #int i,j,k 
        #print("m type",type(m))
        i=m-1
        j=n-1
        k=m+n-1
    
        #Merge num1 and num2 starting from end
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]= nums2[j]
                j-=1    
            k-=1    
        
        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1
        print(nums1)    

solution=Solution()

nums1=[2,3,5,0,0,0]
m=3
nums2=[1,8,9]
n=3
#self=0
solution.merge(nums1,m,nums2,n)