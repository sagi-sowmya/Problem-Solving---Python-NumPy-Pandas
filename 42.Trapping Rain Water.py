#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 12:04:50 2025

@author: sowmya
"""

class Solution:
    def trap(self, height) -> int:
        output=0
        water_level=0
        previous_high=0
        dummy=[]
        #print(len(height)-1)
        for i in range (len(height)-1):
            print(i)
            print("water level",water_level)
            if height[i]==water_level==0:
                print("null")
            elif (height[i]>previous_high) and water_level==0:
                previous_high=height[i]
                dummy.insert(-1,height[i])

            elif (height[i]>previous_high) and water_level!=0:
                previous_high=height[i]
                output+=water_level
                water_level=0
                dummy=[]
                dummy.insert(-1,height[i])

            elif height[i]<=previous_high:
                water_level+=previous_high-height[i]
                dummy.insert(-1,height[i])  
        return output

solution=Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print("Amount of water trapped: ",solution.trap(height))        
        