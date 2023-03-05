class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create an empty dictionary to store characters and their indices
        char_dict = {}
        
        # initialize variables for the start of the substring and the maximum length
        start = 0
        max_len = 0
        
        # loop through each character in the string
        for i in range(len(s)):
            # if the current character is already in the dictionary and its index is greater than or equal to the start of the substring
            if s[i] in char_dict and char_dict[s[i]] >= start:
                # update the start of the substring to the index of the repeated character + 1
                start = char_dict[s[i]] + 1
            # add the current character and its index to the dictionary
            char_dict[s[i]] = i
            # update the maximum length of the substring
            max_len = max(max_len, i - start + 1)
        
        # return the maximum length of the substring
        return max_len
