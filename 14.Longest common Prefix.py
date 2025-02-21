#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:03:09 2025

@author: sowmya
"""

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        prefix=""
        if len(strs)<=1:
            return strs[0]
        else:    
            for i in range(len(strs[0])):
                for j in range(len(strs)):
                    if i<len(strs[j]) and strs[0][i]==strs[j][i] and strs[0][i]!="" and strs[j][i]!="" :
                        if j==len(strs)-1:
                            prefix+=strs[0][i]
                    else:
                        prefix+=""
                        return prefix        
        return prefix 

solution=Solution()
strs=["","",""]

print("Longest common prefix: ",solution.longestCommonPrefix(strs))        
   