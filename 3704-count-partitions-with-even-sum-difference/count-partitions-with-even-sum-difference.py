class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        result = 0

        left_sum, right_sum = 0, sum(nums)

        for index in range(len(nums)-1):
            left_sum += nums[index]
            right_sum -= nums[index]

            if (left_sum - right_sum) % 2 == 0:
                result += 1
        
        return result