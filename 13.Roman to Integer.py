#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:01:01 2025

@author: sowmya
"""

class Solution(object):
    def romanToInt(self, s):
    
        """
        :type s: str
        :rtype: int
        """
        roman='IVXLCDM'
        value=[1,5,10,50,100,500,1000]
        roman_dict = dict(zip(roman, value))
        output=0
        i=0
        while i < (len(s)):
            print("hi :",roman_dict[s[i]])
            print(output)
            print(i)
            if i== len(s)-1:
                output+=roman_dict[s[i]]
            else:    
                if s[i]=='I':
                    if s[i+1] in 'VX':
                        output+= roman_dict[s[i+1]]-roman_dict[s[i]]
                        i+=1
                        print("loop i:",i)
                    elif roman_dict[s[i]]>=roman_dict[s[i+1]]:
                        output+=roman_dict[s[i]]     
                    else:
                        print("Invalid Roman Numeral")
                        return 0  
    
                elif s[i]=='X':
                    if s[i+1] in 'LC':
                        output+= roman_dict[s[i+1]]-roman_dict[s[i]]
                        i+=1
                        print("loop i:",i)
                    elif roman_dict[s[i]]>=roman_dict[s[i+1]]:
                        output+=roman_dict[s[i]]     
                    else:
                        print("Invalid Roman Numeral")
                        return 0 
    
                elif s[i]=='C':
                    if s[i+1] in 'DM':
                        output+= roman_dict[s[i+1]]-roman_dict[s[i]]
                        i+=1
                        print("loop i:",i)
                    elif roman_dict[s[i]]>=roman_dict[s[i+1]]:
                        output+=roman_dict[s[i]]     
                    else:
                        print("Invalid Roman Numeral")
                        return 0 
                else:
                    output+=roman_dict[s[i]]
            i+=1                 
        return output           
solution=Solution()
s="III"
print("Roman equivalent Integer value:",solution.romanToInt(s))   