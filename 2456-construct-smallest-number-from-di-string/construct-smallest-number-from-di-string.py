class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern) + 1
        self.result = []
        self.backtrack(pattern, [], set())
        return ''.join(self.result)
    
    def backtrack(self, pattern, nums, used_digits):
        if len(nums) == len(pattern) + 1:
            res = ''.join(nums)

            if not self.result or res < ''.join(self.result):
                self.result = nums[:]
            return

        for i in range(1, len(pattern) + 2):
            if str(i) not in used_digits:
                nums.append(str(i))
                used_digits.add(str(i))
                if self.isValid(pattern, nums):
                    self.backtrack(pattern, nums, used_digits)
                nums.pop()
                used_digits.remove(str(i))
    

    def isValid(self, pattern, nums):
        for i in range(len(nums) - 1):
            if pattern[i] == 'I' and nums[i] >= nums[i + 1]:
                return False
            if pattern[i] == 'D' and nums[i] <= nums[i + 1]:
                return False
        return True
