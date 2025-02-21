#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:04:38 2025

@author: sowmya
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m=len(needle)
        n=len(haystack)
        for start in range (0,(n-m)+1):
            for i in range (0,m):
                if(needle[i]!=haystack[start+i]):
                    break
                if (i==m-1):
                    return start
        return -1                
        #output=haystack.find(needle)
        #return output



solution=Solution()
haystack="alovera"        
needle="over"
print("The first occurance of needle in haystack is:",solution.strStr(haystack,needle))
        