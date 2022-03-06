class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        cols = {"type": 0, "color": 1, "name": 2}

        for item in items:
            if item[cols[ruleKey]] == ruleValue:
                count += 1

        return count