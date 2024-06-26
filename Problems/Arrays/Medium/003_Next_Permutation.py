# Date solved: 30th May 2024

# Specific Algorithm Used : Narayan Pandita Algorithm (Without this algo it's not possible to solve this problem and you have to learn the algo.)

# Language used to solve: Python and C++

# Problem Description:

# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

# Solution 1 (Python) : 

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        k, l = -1, -1

        for k in range(n - 2, -1, -1):
            if nums[k] < nums[k + 1]:
                break
        else:
            nums.reverse()
            return

        for l in range(n - 1, k, -1):
            if nums[l] > nums[k]:
                break

        nums[k], nums[l] = nums[l], nums[k]

        nums[k + 1:] = reversed(nums[k + 1:])


# Solution 2 (C++) :

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size(), k, l;
        for(k=n-2;k>=0;k--) {
            if(nums[k] < nums[k+1])
                break;
        }
        if(k==-1)
            reverse(nums.begin(), nums.end());
        else {
            for(l=n-1;l>k;l--) {
                if(nums[l] > nums[k])
                    break;
            }
            swap(nums[k], nums[l]);
            reverse(nums.begin() + k + 1, nums.end());
        }
    }
};
