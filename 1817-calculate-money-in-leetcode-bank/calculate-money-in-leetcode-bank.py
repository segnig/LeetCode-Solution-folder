class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0

        for i in range(n):
            result += ((i // 7) + 1 + (i % 7))
        return result
        