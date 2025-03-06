class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        prev_smaller = [-1] * n
        stack = []
        stack_next = []
        next_smaller = [n] * n
        
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            while stack_next and nums[stack_next[-1]] > nums[n - 1 - i]:
                stack_next.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            if stack_next:
                next_smaller[n - i - 1] = stack_next[-1]
            stack_next.append(n - i - 1)
            stack.append(i)
        result = sum(
            [(i - prev_smaller[i]) * (next_smaller[i] - i) * nums[i] for i in range(n)]
        )
        return result % MOD