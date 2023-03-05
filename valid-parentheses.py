class Solution:
    def isValid(self, s: str) -> bool:
        # Create a dictionary to map closing brackets to their corresponding
        # opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        # Create a stack to keep track of opening brackets
        stack = []
        # Iterate through each character in the string
        for char in s:
            # If the character is an opening bracket, push it onto the stack
            if char in bracket_map.values():
                stack.append(char)
            # If the character is a closing bracket, check if it matches the top
            # of the stack
            elif char in bracket_map.keys():
                # If the stack is empty or the top of the stack doesn't match
                # the closing bracket, return False
                if not stack or bracket_map[char] != stack[-1]:
                    return False
                # Otherwise, pop the top of the stack
                else:
                    stack.pop()
        # If the stack is empty, all opening brackets have been matched with
        # closing brackets, so return True Otherwise, there are still unmatched
        # opening brackets, so return False
        return not stack
