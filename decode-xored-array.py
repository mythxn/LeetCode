class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        decoded = [first]
        for i in range(len(encoded)):
            decoded.append(encoded[i] ^ decoded[i])
        return decoded