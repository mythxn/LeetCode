# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy head node to make it easier to merge the two lists
        dummy_head = ListNode(0)
        current_node = dummy_head

        # Loop while both lists are not empty
        while l1 and l2:
            # Compare the values of the first nodes of each list
            if l1.val <= l2.val:
                # l1's node should come first in the merged list
                current_node.next = l1
                l1 = l1.next
            else:
                # l2's node should come first in the merged list
                current_node.next = l2
                l2 = l2.next

            # Move to the next node in the merged list
            current_node = current_node.next

        # Attach the remaining nodes of either list, if any
        current_node.next = l1 or l2
        # Return the head node of the merged list (after the dummy head)
        return dummy_head.next
