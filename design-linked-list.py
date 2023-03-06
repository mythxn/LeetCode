class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # value of node
        self.next = next    # pointer to the next node (default is None)


class MyLinkedList:
    def __init__(self):
        """
        Initialize your linked list here.
        """
        self.head = None    # set the head to None (empty list)
        self.length = 0     # set the length of the list to 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length:  # check if index is out of bounds
            return -1
        current = self.head     # set current node to head
        for _ in range(index):
            current = current.next
        return current.val      # return the value of the index-th node

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        new_node = ListNode(val)    # create a new node with the given value
        new_node.next = self.head   # point the new node to the current head
        self.head = new_node        # set the head to the new node
        self.length += 1            # increment the length of the list

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head is None:        # if the list is empty, add the new node at the head
            self.addAtHead(val)
        else:
            current = self.head      # set current node to head
            while current.next:      # iterate through list until we get to the last node
                current = current.next
            new_node = ListNode(val) # create a new node with the given value
            current.next = new_node  # point the last node to the new node
            self.length += 1         # increment the length of the list

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.length:    # check if index is out of bounds
            return
        elif index == 0:                        # if index is 0, add node at the head
            self.addAtHead(val)
        elif index == self.length:              # if index is equal to the length, add node at the tail
            self.addAtTail(val)
        else:
            current = self.head                 # set current node to head
            for _ in range(index-1):            # iterate through list until we get to the node before the index-th node
                current = current.next
            new_node = ListNode(val)            # create a new node with the given value
            new_node.next = current.next        # point the new node to the index-th node
            current.next = new_node             # point the node before the index-th node to the new node
            self.length += 1                    # increment the length of the list
            
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.length:    # check if index is out of bounds
            return
        elif index == 0:                         # if index is 0, delete the head
            self.head = self.head.next
        else:
            current = self.head                  # set current node to head
            for _ in range(index-1):             # iterate through list until we get to the node before the index-th node
                current = current.next
            current.next = current.next.next     # point the node before the index-th node to the node after the index-th node
        self.length -= 1                         # decrement the length of the list
