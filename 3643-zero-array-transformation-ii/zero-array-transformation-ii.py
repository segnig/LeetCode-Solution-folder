class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        left = 0
        right = len(queries)
        best = -1

        while left <= right:
            mid = left + (right - left) // 2
            print(mid)
            if self.check(nums, queries[:mid]):
                right = mid - 1
                best = mid
            else:
                left = mid + 1
        return best 
    
    def check(self, given, queries):
        nums = given.copy()
        nums = [0] * (len(given) + 1)

        for left, right, val in queries:
            nums[left] -= val
            nums[right + 1] += val

        prev = 0
        for i in range(len(given)):
            prev = nums[i] + prev
            if prev + given[i] > 0:
                return False 
        return True   