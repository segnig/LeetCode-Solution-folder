class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcf(a, b):
            if b == 0:
                return a
            return gcf(b, a%b)

        max_num = max(nums)
        min_num = min(nums)

        return gcf(max_num, min_num)

    
        