class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        
        def helper(mid):

            difference = 0

            for x0, y0, length in squares:

                yf = y0 + length

                if yf > mid > y0:
                    difference += (mid - y0) * length
                    difference -= (yf - mid) * length
                elif yf <= mid:
                    difference += length * length
                else:
                    difference -= length * length

            return difference >= 0

        
        right, left = 10 ** 9 + 1, 0

        while right - left >= 0.000001:
            mid = left + (right- left) / 2

            if helper(mid):
                right = mid
            else:
                left = mid
        return left 