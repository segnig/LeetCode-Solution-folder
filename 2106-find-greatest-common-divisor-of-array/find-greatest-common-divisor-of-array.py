class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return self.gcf(min(nums), max(nums))

    

    def gcf(self, num1, num2):
        if num2 == 0:
            return num1

        return self.gcf(num2, num1 % num2)