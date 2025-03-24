class Solution:
    def mySqrt(self, n: int) -> int:
        left = 0
        right = n

        while left<= right:
            mid = (left + right) // 2
            if mid * mid == n:
                return mid
            elif mid * mid < n:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1