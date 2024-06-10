# Date solved: 10th June 2024

# Language used to solve: Python

# Problem Description:

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Solution 1 (Python) : 

# Time complexity : O(max(n,m))
# Space complexity : O(max(n,m))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        tail, carry = dummyHead, 0
        while l1 or l2 or carry:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            sum = digit1 + digit2 + carry
            unitDigit = sum % 10
            carry = sum // 10
            tail.next = ListNode(unitDigit)
            tail = tail.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummyHead.next

# Let 𝑛 be the length of l1 and 𝑚 be the length of l2.

# The loop runs for a maximum of max(n,m)+1 iterations because the carry might add an extra iteration at the end.
# Therefore, the time complexity is O(max(n,m))

# The function creates a new linked list to store the result.
# The number of nodes in the result linked list is at most max(n,m)+1 (the extra node is for the carry if it exists).
# Therefore, the extra space complexity is dominated by the space required for the result linked list, which is O(max(n,m)).
