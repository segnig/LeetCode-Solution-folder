class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[mid] < target:
                    left = mid + 1
                elif nums[left] > target:
                    left = mid + 1
                else:
                    right = mid - 1 
            else:
                if nums[mid] > target:
                    right = mid - 1
                elif nums[right] < target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1