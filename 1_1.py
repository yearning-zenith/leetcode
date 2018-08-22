#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 16:39:53 2018

@author: yearning_zenith
"""
c = [2, 7, 11, 15]
d = 9

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    a=[i,j]                    
        return a
    
b=Solution().twoSum(c,d);