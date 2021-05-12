#
# @lc app=leetcode id=1720 lang=python3
#
# [1720] Decode XORed Array
#

# @lc code=start
class Solution:
    def decode(self, encoded, first):
        arr = [first]

        for i in range(len(encoded)):
            arr.append(arr[i] ^ encoded[i])

        return arr


# @lc code=end
