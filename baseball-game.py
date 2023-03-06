from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []  # Initialize stack to keep track of valid points

        for op in ops:
            if op == "C":  # If the last score is invalid, remove it from stack
                stack.pop()
            elif op == "D":  # Double the last score and add it to stack
                stack.append(stack[-1] * 2)
            elif op == "+":  # Add the sum of last two scores and add it to stack
                stack.append(stack[-1] + stack[-2])
            else:  # The score is a valid integer, add it to stack
                stack.append(int(op))

        return sum(stack)  # Return the sum of all valid scores in stack
