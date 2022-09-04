class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        neg = num < 0
        out = ""

        while abs(num) > 0:
            rem = abs(num) % 7
            out += str(rem)
            num = abs(num) // 7

        if not neg:
            return out[::-1]
        else:
            return "-" + out[::-1]
