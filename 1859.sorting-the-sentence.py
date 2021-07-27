#
# @lc app=leetcode id=1859 lang=python3
#
# [1859] Sorting the Sentence
#

# @lc code=start
class Solution:
    def sortSentence(self, s: str) -> str:
        ord_map = {word[-1]: word[:-1] for word in s.split()}
        sorted_words = [sort_lst[1] for sort_lst in sorted(ord_map.items())]
        return " ".join(sorted_words)


# @lc code=end
