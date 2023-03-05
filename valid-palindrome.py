class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert the input string to lowercase and remove non-alphanumeric characters
        s = ''.join(c for c in s.lower() if c.isalnum())

        # Check if the resulting string is equal to its reverse
        return s == s[::-1]
