#
# @lc app=leetcode id=1773 lang=python3
#
# [1773] Count Items Matching a Rule
#

# @lc code=start
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cols = {"type": 0, "color": 1, "name": 2}

        return sum(item[cols[ruleKey]] == ruleValue for item in items)


# @lc code=end
