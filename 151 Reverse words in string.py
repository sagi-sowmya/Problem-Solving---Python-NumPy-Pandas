#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:04:29 2025

@author: sowmya
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        n=len(s)
        i=0
        if n<=1:
            return " ".join(s)
        else:    
            while i<=(n/2):
                dummy=s[i]
                s[i]=s[n-i-1]
                s[n-i-1]=dummy
                i+=1
                
                if (i==(n-1)/2) or (i==n/2):
                    return " ".join(s) 
            
solution=Solution()
s="the sky is blue"
print("Reversed string: ",solution.reverseWords(s)) 
