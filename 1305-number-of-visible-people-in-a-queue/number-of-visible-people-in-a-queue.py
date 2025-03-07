class Solution:
    def canSeePersonsCount(self, nums: List[int]) -> List[int]:
        stack = []
        result = [0] * len(nums)

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                popped = stack.pop()
                result[popped] += 1
            if stack:
                result[stack[-1]] += 1
            stack.append(i)
        print(result)
        return result