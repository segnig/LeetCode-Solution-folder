class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = 0
        mini, maxi, badi = -1, -1, -1
        n = len(nums)

        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                badi = i
            if nums[i] == maxK:
                maxi = i
            if nums[i] == minK:
                mini = i
            result += max(0, min(mini, maxi) - badi)
        return result 