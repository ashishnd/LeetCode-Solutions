# Date solved: 6th June 2024

# Language used to solve: Python

# Problem Description:

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Example 1:

# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:

# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

# Solution 1 (Python) : 

# Time Complexity : O(N)
# Space Complexity : O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head

# Why time complexity is O(N) even though there is nested while loop?
# The time complexity of the given code is O(n), where n is the number of nodes in the linked list. Here's why:

# The outer while cur loop runs through each node of the linked list exactly once.

# The inner while cur.next and cur.next.val == cur.val loop, in the worst case, also runs through each node exactly once, but this happens only when there are duplicates. Even if duplicates are present, each node is visited and processed a fixed number of times (in this case, once for comparison and possibly once for skipping the duplicate).

# Since each node is processed a constant number of times, the overall time complexity is linear, O(n).
