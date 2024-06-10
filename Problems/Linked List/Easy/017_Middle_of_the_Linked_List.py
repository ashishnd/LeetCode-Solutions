# Date solved: 9th June 2024

# Language used to solve: Python

# Problem Description:

# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.
  
# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example 2:

# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# Constraints:

# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100

# Solution 1 (Python) (Floyd's cycle detection algo./Tortoise and Hare algo.) : 

# Time Complexity : O(N)
# Space Complexity : O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# How is the time complexity O(N) when the number of times the loop runs in only N/2 times because when the slow reaches middle then fast reaches end 
# and the loop stops, so shouldn't the time complexity be O(N/2)?

# ChatGPT Answer

# While it is true that the loop runs N/2 times, Big-O notation abstracts away constant factors.
# O(N/2) is simplified to O(N) in Big-O notation because Big-O notation focuses on the dominant term and ignores constant factors.
