#
# @lc app=leetcode id=838 lang=python3
#
# [838] Push Dominoes
#

# @lc code=start
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        while True:
            # standing
            step = dominoes.replace('R.L', 'S')

            # left / right
            step = step.replace('.L', 'LL')
            step = step.replace('R.', 'RR')

            # until all dominoes have fallen
            if step == dominoes:
                break
            else:
                dominoes = step

        # correct standing domino notation
        return dominoes.replace('S', 'R.L')

# @lc code=end
