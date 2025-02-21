#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:59:51 2025

@author: sowmya
"""

class Solution(object):
    def maxProfit(self, prices):
            profit=0
            max_profit=0
            mini=float('inf')
            for i in range(0,len(prices)):
                if prices[i]< mini:
                    mini=prices[i]
                elif prices[i] - mini >= profit:
                    profit = prices[i]-mini
                    max_profit += profit
                    profit=0
                    mini=prices[i]

                

                #maxi=max(prices[i+1:len(prices)])
                #profit=maxi-mini
            
                #if profit > max_profit:
                 #   max_profit = profit
            return max_profit       

solution=Solution()
prices=[73,7,9,0,0,8,9]
print("Maximum profit achieved:", solution.maxProfit(prices) )  

        