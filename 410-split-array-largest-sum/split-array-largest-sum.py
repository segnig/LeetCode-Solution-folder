class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = (left + right) // 2
            if self.check(nums, k, mid):
                right = mid - 1
            else:
                left = mid + 1
            
        return left


    def check(self, nums, k, limit):
        count = 1
        sum_ = 0

        for num in nums:
            if num + sum_ > limit:
                count += 1
                sum_ = num
            else:
                sum_ += num
        return count <= k