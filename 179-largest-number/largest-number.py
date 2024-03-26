class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def compare(x, y):
            return int(y + x) - int(x + y)
        nums = [str(num) for num in nums]
        nums.sort(key=lambda x: x*9, reverse=True)

        result = ''.join(nums)
        result = result.lstrip('0')

        return result if result else '0'
