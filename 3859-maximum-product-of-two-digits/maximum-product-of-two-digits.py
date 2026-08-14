class Solution:
    def maxProduct(self, n: int) -> int:
        nums = []

        for d in str(n):
            nums.append(int(d))

        nums.sort()

        return nums[-1] * nums[-2]