# Date solved: 11th June 2024

# Language used to solve: Python

# Problem Description:

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:

# Input: head = [1], n = 1
# Output: []

# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

# Follow up: Could you do this in one pass?

# Solution 1 (Python) : 

# Time complexity : O(N)
# Space complexity : O(1)
# Passes required : 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head
        for _ in range(n): fast = fast.next
        if not fast: return head.next
        while fast.next: fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head

# Solution 2 (Python) (Trivial/Naive Solution) : 

# Time complexity : O(N)
# Space complexity : O(1)
# Passes required : 2 (inefficient)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead.next = head
        cur = dummyHead
        count = 0
        while cur:
            count += 1
            cur = cur.next
        cur = dummyHead
        total = count-1-n
        while total:

            cur = cur.next
            total -= 1
        cur.next = cur.next.next
        return dummyHead.next
