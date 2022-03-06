class Solution:
    def addDigits(self, num: int) -> int:
        sum = self.str_to_sum(num)
        while len(str(sum)) != 1:
            sum = self.str_to_sum(sum)
        return sum

    def str_to_sum(self, n: int) -> int:
        string = str(n)
        return sum(int(char) for char in string)