#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 13:09:20 2025

@author: sowmya
"""

class Solution(object):
    def maxProfit(self, prices):

        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2: return 0
        min=prices[0]
        max=prices[1]
        j,k=0,0
        for i in range(0,len(prices)):
            min, j = (prices[i], i) if min >= prices[i] else (min, j)
            #max=prices[i+1],k+=1 if max<prices[i]
        for i in range(1,len(prices)):
            #min=prices[i],j+=1 if min>prices[i]
            print("ji")
            max, k = (prices[i], i) if max<=prices[i] else (max,k)
        print(j,k)
        if min<max and j<k:
            profit= max-min
        else:
            profit=0
        return profit        

solution=Solution()
prices=[1,2]

print("Maximum profit achieved:", solution.maxProfit(prices) )   


    

""""""""" Approach 1
class Solution(object):
    def maxProfit(self, prices):

        mini=prices[0]
        maxi=prices[0]
        profit=[]
        j,k=0,0
        if len(prices)<2 or len(prices)>10**5 or max(prices)>10**4: 
            return 0
        else: 
           
            for i in range(0,len(prices)-1):
                mini=prices[i]
                maxi=max(prices[i:len(prices)])
    
                if mini<maxi:
                    profit.append(maxi-mini)
                else:
                    profit.append(0)
            print(profit)
            return max(profit)        

solution=Solution()
prices=[73,7,9,0,0,8,9]

print("Maximum profit achieved:", solution.maxProfit(prices) )      

""""

"""Approach 2
class Solution(object):
    def maxProfit(self, prices):
            max_profit=0
            
            for i in range(0,len(prices)-1):
                mini=prices[i]
          

                maxi=max(prices[i+1:len(prices)])
                profit=maxi-mini
            
                if profit > max_profit:
                    max_profit = profit
            return max_profit       

solution=Solution()
prices=[73,7,9,0,0,8,9]
print("Maximum profit achieved:", solution.maxProfit(prices) )  
"""
