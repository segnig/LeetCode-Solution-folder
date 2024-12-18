class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = k

        left = right = res = 0

        while right < len(nums):
            if nums[right] == 0:
                zeros -= 1
            while zeros < 0:
                if nums[left] == 0:
                    zeros += 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res