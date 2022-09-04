class Solution:
    def convertBinaryToBase6(self, num):
        decimal = self.any_base_to_decimal(num, 2)
        return self.decimal_to_any_base(decimal, 6)

    def any_base_to_decimal(self, num, base):
        decimal = 0
        for i in range(len(num)):
            decimal += int(num[i]) * (base ** (len(num) - i - 1))
        return decimal

    def decimal_to_any_base(self, num, base):
        if num == 0:
            return '0'
        result = ''
        while num > 0:
            result = str(num % base) + result
            num = num // base
        return result
