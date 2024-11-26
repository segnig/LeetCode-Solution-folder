class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0

        for i in range(len(nums) - 1):
            answer = max(answer,  nums[i + 1] - nums[i])
        return answer