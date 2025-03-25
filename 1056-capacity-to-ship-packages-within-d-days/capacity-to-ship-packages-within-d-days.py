class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right, best = max(weights), sum(weights), -1

        while left <= right:
            mid = (left + right) // 2
            days_takes = 1
            cummulate = 0
            for weight in weights:
                cummulate += weight
                if cummulate > mid:
                    days_takes += 1
                    cummulate = weight
            
            if days_takes > days:
                left = mid + 1
            else:
                best = mid
                right = mid - 1
        return left     