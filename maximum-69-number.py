class Solution:
    def maximum69Number(self, num):
        sanitized_num = list(str(num))
        for i, val in enumerate(sanitized_num):
            if val != '9':
                sanitized_num[i] = '9'
        return ''.join(sanitized_num)
