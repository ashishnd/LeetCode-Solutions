# Date solved: 12th June 2024

# Language used to solve: Python

# Problem Description:

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:

# Input: lists = []
# Output: []

# Example 3:

# Input: lists = [[]]
# Output: []

# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.


# Solution 1 (Python) (My solution, Not very efficient) : 

# Time complexity : O(Nk^2)
# Space complexity : O(1) (auxiliary space) and O(Nk) for the merged list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None
        if len(lists) == 1: return lists[0]
        lst = 0
        for lst in range(0, len(lists)-1):
            list1 = lists[lst]
            list2 = lists[lst+1]
            cur = dummy = ListNode()
            while list1 and list2:
                if(list1.val < list2.val):
                    cur.next = list1
                    list1 = list1.next
                    cur = cur.next
                else:
                    cur.next = list2
                    list2 = list2.next
                    cur = cur.next
            if list1 or list2:
                cur.next = list1 if list1 else list2
            lists[lst+1] = dummy.next
        return lists[lst+1]


# Solution 2 (Python) (Efficient Solution) : 

# Time complexity : O()
# Space complexity : O()
