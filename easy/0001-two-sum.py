"""
Problem: Two Sum
LeetCode: https://leetcode.com/problems/two-sum/
Level: Easy

Description:
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice. You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Approach:
Iterate through the list while using a dictionary to store the index of each 
element. For each number, check if the complement (target - current number)
is already in the dictionary. If it is, return the indices.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in dic:
                return [dic[diff], i]
            else:
                dic[nums[i]] = i