class MinStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []  # main stack to hold all elements
        self.min_stack = []  # auxiliary stack to hold minimum values

    def push(self, val: int) -> None:
        """
        Push element val onto stack.
        """
        self.stack.append(val)  # push val onto main stack

        # check if val is smaller than or equal to current minimum
        # if so, push it onto min_stack as well
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """
        Removes the element on the top of the stack.
        """
        val = self.stack.pop()  # remove top element from main stack

        # if val is equal to the current minimum, remove it from min_stack as well
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        """
        Get the top element of the stack.
        """
        return self.stack[-1]  # return top element of main stack

    def getMin(self) -> int:
        """
        Retrieve the minimum element in the stack.
        """
        return self.min_stack[-1]  # return top element of min_stack
