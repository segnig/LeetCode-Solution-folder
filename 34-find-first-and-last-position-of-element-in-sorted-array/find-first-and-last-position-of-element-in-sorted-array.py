class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.lower(nums, target), self.upper(nums, target)]

    def lower(self, nums, target):
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                result = mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    def upper(self, nums, target):
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                result = mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return result