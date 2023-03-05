from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Given an array of strings 'strs', group the anagrams together. An
        anagram is a word or phrase formed by rearranging the letters of a
        different word or phrase, typically using all the original letters
        exactly once. You can return the answer in any order.
        """
        # Create an empty dictionary to store the anagram groups
        anagram_dict = {}

        # Loop through each string in the input list
        for word in strs:
            # Sort the letters in the current string and use it as a key in the
            # dictionary The value for this key will be a list of strings that
            # are anagrams of each other
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]

        # Return the values of the dictionary as a list of lists
        return list(anagram_dict.values())
