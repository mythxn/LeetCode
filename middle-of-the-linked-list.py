class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_po, fast_po = head, head

        while slow_po and fast_po and fast_po.next:
            slow_po = slow_po.next
            fast_po = fast_po.next.next

        return slow_po
