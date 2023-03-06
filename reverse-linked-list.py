# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # If the input linked list is empty or has only one node,
        # it is already reversed, so return the original linked list
        if not head or not head.next:
            return head

        # Initialize the previous node to None, the current node to head,
        # and the next node to head's next node
        prev_node = None
        curr_node = head
        next_node = head.next

        # Traverse the linked list, reversing the direction of the links
        while next_node:
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            next_node = next_node.next

        # Once the traversal is complete, set the final node's next pointer to
        # the previous node (which will be the new head of the reversed linked list)
        curr_node.next = prev_node

        # Return the new head of the reversed linked list
        return curr_node
