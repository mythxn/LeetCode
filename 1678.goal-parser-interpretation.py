#
# @lc app=leetcode id=1678 lang=python3
#
# [1678] Goal Parser Interpretation
#

# @lc code=start
class Solution:
    def interpret(self, command: str) -> str:

        legend = {"G": "G", "()": "o", "(al)": "al"}

        for key in legend.keys():
            command = command.replace(key, legend[key])

        return command


# @lc code=end
