class Solution:
    def sortSentence(self, s: str) -> str:
        ord_map = {word[-1]: word[:-1] for word in s.split()}
        sorted_words = [sort_lst[1] for sort_lst in sorted(ord_map.items())]
        return " ".join(sorted_words)
