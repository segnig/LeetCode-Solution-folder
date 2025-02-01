class Solution(object):
    def plusOne(self, digits):
        result = []
        remainder = 1
        for n in digits[::-1]:
            res = n + remainder
            remainder = res // 10
            result.append(res % 10)
        if remainder:
            result.append(remainder)

        return result[::-1]