class Solution:
    def decode(self, encoded, first):
        arr = [first]

        for i in range(len(encoded)):
            arr.append(arr[i] ^ encoded[i])

        return arr