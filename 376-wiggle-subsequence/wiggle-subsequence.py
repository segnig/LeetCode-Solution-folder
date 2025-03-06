class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        result = 1
        difference = [
            nums[i + 1] - nums[i] < 0 for i in range(len(nums) - 1) if nums[i + 1] - nums[i] != 0
        ]
        print(difference)
        stack = []
        for diff in difference:
            if stack and stack[-1] == diff:
                result = max(result, len(stack) + 1)
            else:
                stack.append(diff)
                result = max(result, len(stack) + 1)

        return result