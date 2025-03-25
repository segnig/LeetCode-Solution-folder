class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = sum(piles)
        best = 0

        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += ceil(pile / mid)
            if hours > h:
                left = mid + 1
            else:
                best = mid 
                right = mid - 1

        return best