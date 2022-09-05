class Solution(object):
    def convertToBase6(self, num):
        """
        :type num: int
        :rtype: str
        """
        return self.any_number_to_any_base(num, 6)

    def any_number_to_any_base(self, num, base):
        if num == 0:
            return "0"
        neg = num < 0
        out = ""
        while abs(num) > 0:
            rem = abs(num) % base
            out += str(rem)
            num = abs(num) // base
        return f"-{out[::-1]}" if neg else out[::-1]