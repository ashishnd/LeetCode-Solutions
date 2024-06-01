# Date solved: 1st June 2024

# Language used to solve: Python and C++

# Problem Description:

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
  
# Solution 1 (Python) : 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax, globalMax = nums[0], nums[0]
        for i in range(1, len(nums)):
            currMax = max(currMax + nums[i], nums[i])
            globalMax = max(globalMax, currMax)
        return globalMax

# Solution 2 (C++) :

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currSum = nums[0], globalMaxSum = nums[0];
        for(int i = 1; i < nums.size(); i++) {
            currSum = max(currSum + nums[i], nums[i]);
            globalMaxSum = max(globalMaxSum, currSum);
        }
        return globalMaxSum;
    }
};
