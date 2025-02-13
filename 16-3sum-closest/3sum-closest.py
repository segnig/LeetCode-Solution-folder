class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = sum(nums[:3])
        print(result)
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum_lr = nums[left] + nums[right]
                if abs(target - result)  > abs(target - (sum_lr + nums[i])):
                    result = sum_lr + nums[i]
                if sum_lr + nums[i] > target:
                    right -= 1
                else:
                    left += 1
        return result

        