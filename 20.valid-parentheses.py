#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        stack = []

        for c in s:
            if c in brackets:
                stack.append(brackets[c])
            elif not stack or stack.pop() != c:
                return False

        return not stack

# @lc code=end
