#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:02:29 2025

@author: sowmya
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        i=len(s)-1
        while i>=0 and s[i]!=" ":
            i-=1
        return len(s)-i-1   

        
solution=Solution()
s="I'm a very good girl."
print("Length of last word is: ",solution.lengthOfLastWord(s))        