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


# Solution 2 (Python) (Efficient Solution) (Divide and Conquer) : 

# Time complexity : O(Nlogk)
# Space complexity : O(logk)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)
    # 1st way (iterative)
    def merge(self, l, r):
        dummy = p = ListNode()
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next
    # 2nd way (recursive)
    def merge1(self, l, r):
        if not l or not r:
            return l or r
        if l.val< r.val:
            l.next = self.merge(l.next, r)
            return l
        r.next = self.merge(l, r.next)
        return r

# Complexity Explanation
# The provided code merges k sorted linked lists using a divide-and-conquer approach, similar to the merge sort algorithm.

# Base Case:

# If the input list of lists is empty, return None.
# If the input list contains only one list, return that list.

# Recursive Case:

# Split the list of lists into two halves.
# Recursively merge the left and right halves.
# Merge the two sorted halves using the merge function.

# Merging Two Lists
# The merge function merges two sorted linked lists and returns the merged list.

# Time Complexity

# Dividing the List:

# The list of lists is divided into halves at each level of recursion.
# The depth of the recursion tree is logk because the list is halved at each step.

# Merging Lists:

# At each level of the recursion tree, every node in the k lists is processed once.
# Merging two lists takes O(N), where N is the total number of nodes in the lists being merged.
# At each level of the recursion tree, the total number of nodes processed is O(N).

# Total Time Complexity:

# The total time complexity is O(Nlogk), where N is the total number of nodes across all k lists.

# Space Complexity

# Auxiliary Space for Recursion:

# The recursion depth is logk.
# Each recursive call uses a constant amount of space, so the auxiliary space complexity for the recursion is O(logk).

# Auxiliary Space for Merging:

# The merge function uses a constant amount of space for pointers.

# Total Space Complexity:

# The total auxiliary space complexity is O(logk) due to the recursion depth.

# Summary
# Time Complexity: O(Nlogk)
# The list of lists is divided and merged in a manner similar to merge sort, resulting in a logarithmic depth recursion tree with linear merging at each level.

# Space Complexity: O(logk)
# The space complexity is dominated by the recursion depth, which is logarithmic with respect to the number of lists.
