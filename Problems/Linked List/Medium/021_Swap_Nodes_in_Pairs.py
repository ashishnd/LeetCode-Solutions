# Date solved: 14th June 2024

# Language used to solve: Python

# Problem Description:

# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's 
# nodes (i.e., only nodes themselves may be changed.)

# Example 1:

# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

# Example 2:

# Input: head = []
# Output: []

# Example 3:

# Input: head = [1]
# Output: [1]

# Constraints:

# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100


# Solution 1 (Python) : 

# Time complexity : O(N)
# Space complexity : O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next
