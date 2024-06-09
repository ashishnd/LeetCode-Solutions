# IMPORTANT

# Date solved: 9th June 2024

# Language used to solve: Python

# Problem Description:

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
  
# Example 1:

# Input: head = [1,2,2,1]
# Output: true

# Example 2:

# Input: head = [1,2]
# Output: false

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9

# Follow up: Could you do it in O(n) time and O(1) space?

# Solution 1 (Python) (Floyd's cycle detection(Tortoise and Hare algo. for finding mid) + Reverse linked list(2nd half)) : 

# Time Complexity : O(N)
# Space Complexity : O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow, prev = head, head, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            # This way
            # next_node = slow.next
            # slow.next = prev
            # prev = slow
            # slow = next_node
            # Or this way(Multiple assignment/Tuple assignment)
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val:
                return False
            fast, slow = fast.next, slow.next
        return True

# Time Complexity : O(N)
# Space Complexity : O(1)

# Multiple assignment isn't the same as several assignments one after the other. The difference is that the values on the right hand side of the statement 
# all get evaluated before anything get rebound. The values on the right hand side are in fact packed up in a tuple, then unpacked into the names on the left 
# hand side.

# That's important in this situation as it means that node.next on the right hand side gets its value saved, so that when you rebind it to something else (pre), 
# the old value is still available to become the new node value after the assignment.

# You may want to play around with some simpler assignments, like the classic swap operation:

# x = 1
# y = 2

# x, y = y, x  swap x and y's values

# print(x, y)  prints "2 1"

# _tup = y, x   this is how it works, first pack the RHS values into a tuple
# x, y = _tup   then unpack the values into the names on the LHS

# print(x, y)   prints "1 2" as we've swapped back

# Another thing learnt
# Short-Circuit Evaluation in Python

# If there are even number of nodes in the linked list then after fast reaches None then after that when the while loop condition check is run for the final 
# time it checks for fast and fast.next but when the while loop will try to access fast.next shouldn't it give an exception because fast has already reached 
# None so fast.next will be out of bound?
# ChatGPT Answer
# Great observation! You're right that if fast reaches None, then checking fast.next would indeed cause an error. However, in the condition while fast and fast.next:, Python's short-circuit evaluation prevents this error. Let's break this down.

# In Python, logical operators like and and or use short-circuit evaluation. This means that in an expression with and, if the first operand is False, Python does 
# not evaluate the second operand because the overall result is already determined to be False.
