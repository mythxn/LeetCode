#
# @lc app=leetcode id=1773 lang=python3
#
# [1773] Count Items Matching a Rule
#

# @lc code=start
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        cols = {"type": 0, "color": 1, "name": 2}

        for item in items:
            if item[cols[ruleKey]] == ruleValue:
                count += 1

        return count


# @lc code=end
