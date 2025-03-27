class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        left, right = 1, max(candies)
        while left <= right:
            mid = left + (right - left) // 2
            if self.check(candies, k, mid):
                left = mid + 1
            else:
                right = mid - 1
        return right


    def check(self, candies, k, per_child):
        count = 0
        for cand in candies:
            count += cand // per_child
        
        return count >= k