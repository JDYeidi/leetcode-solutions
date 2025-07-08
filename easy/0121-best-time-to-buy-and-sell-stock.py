"""
Problem: Best Time to Buy and Sell Stock
LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Level: Easy

Description:
You are given an array prices where prices[i] is the price of a given stock...

Example:
Input: prices = [7,1,5,3,6,4]
Output: 5

Approach:
Track minimum price so far, update max profit on each iteration.

Time Complexity: O(n)
Space Complexity: O(1)
"""


from typing import List

def maxProfit(self, prices: List[int]) -> int:
        current_min = float('inf')
        current_profit = 0

        for price in prices:
            if price < current_min:
                current_min = price

            profit = price - current_min
            if profit > current_profit:
                current_profit = profit

        return current_profit