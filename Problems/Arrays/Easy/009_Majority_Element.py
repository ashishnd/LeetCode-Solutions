# Date solved: 4th June 2024

# Language used to solve: Python

# Problem Description:

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3

# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109

# Solution 1 (Python) : 

# Time Complexity : O(n)
# Space Complexity : O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_map = {}
        for num in nums:
            if num in my_map:
                my_map[num] += 1
            else:
                my_map[num] = 1
        for key in my_map:
            if(my_map[key] > len(nums)/2):
                return key
        return 0
