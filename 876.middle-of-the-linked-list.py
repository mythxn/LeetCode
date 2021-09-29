#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_po, fast_po = head, head

        while slow_po and fast_po and fast_po.next:
            slow_po = slow_po.next
            fast_po = fast_po.next.next

        return slow_po



# @lc code=end
