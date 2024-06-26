# IMPORTANT

# Date solved: 7th June 2024

# Specific Algorithm Used : Tortoise and Hare (Floyd’s Cycle Detection)

# Language used to solve: Python

# Problem Description:

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:

# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:

# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# Constraints:

# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.

# Solution 1 (Python) : 

# Time complexity : O(N)
# Space complexity : O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

# NOTE
# Algorithm: Tortoise and Hare (Floyd’s Cycle Detection).
# Key Idea: Use two pointers moving at different speeds. If there is a cycle, they will eventually meet; if not, the fast pointer will reach the end of the list.
# Time Complexity: O(n), where n is the number of nodes in the list.
# Space Complexity: O(1), constant space.
# This algorithm is efficient and elegant for detecting cycles in a linked list.

# Other things learnt in this problem
# Coding approach used in this problem : 

# Easier to Ask for Forgiveness than Permission (EAFP)
# Easier to ask for forgiveness than permission. This common Python coding style assumes the existence of valid keys or attributes and catches exceptions if 
# the assumption proves false. This clean and fast style is characterized by the presence of many try and except statements. The technique contrasts 
# with the LBYL style common to many other languages such as C.

# Other coding approach generally used : 
# Look Before You Leap (LBYL)

# This coding style explicitly tests for pre-conditions before making calls or lookups. This style contrasts with the EAFP approach and is characterized 
# by the presence of many if statements.

# In a multi-threaded environment, the LBYL approach can risk introducing a race condition between “the looking” and “the leaping”. For example, the code,
# if key in mapping: return mapping[key] can fail if another thread removes key from mapping after the test, but before the lookup. This issue can be solved
# with locks or by using the EAFP approach.
