class Solution(object):
    def isCovered(self, ranges, left, right):
        set1 = set()

        for l, r in ranges:
            for num in range(l, r + 1):
                set1.add(num)

        for num in range(left, right + 1):
            if num not in set1:
                return False

        return True