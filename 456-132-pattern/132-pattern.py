class Solution(object):
    def find132pattern(self, nums):
        min_value = float("-inf")
        stack = []

        for num in reversed(nums):
            if num < min_value:
                return True
            while stack and stack[-1] < num:
                min_value = max(min_value, stack.pop())
            stack.append(num)

        return False