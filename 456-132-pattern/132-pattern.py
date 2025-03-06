class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        second_num = float("-inf")
        stack = []

        for num in nums[::-1]:
            if num < second_num:
                return True
            while stack and stack[-1] < num:
                second_num = max(second_num, stack.pop())
            stack.append(num)
        return False