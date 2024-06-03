# Date solved: 3rd June 2024

# Language used to solve: Python

# Problem Description:

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

# Solution 1 (Python) : 

# Time Complexity : O(log(n))
# Space Complexity : O(1)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while(left<=right):
            mid = math.floor((left+right)/2)

            if(target == nums[mid]):
                return mid
            if(target < nums[mid]):
                right = mid-1
            if(target > nums[mid]):
                left = mid+1
        else:    
            return left

