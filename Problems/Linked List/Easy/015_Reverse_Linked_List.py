# Date solved: 9th June 2024

# Language used to solve: Python

# Problem Description:

# Given the head of a singly linked list, reverse the list, and return the reversed list.
  
# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:

# Input: head = [1,2]
# Output: [2,1]

# Example 3:

# Input: head = []
# Output: []

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

# Solution 1 (Python) (iterative) : 

# Time Complexity : O(N)
# Space Complexity : O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, next = None, None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

# Solution 2 (Python) (recursive) :
# Add here
