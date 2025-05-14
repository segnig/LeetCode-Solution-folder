class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        n = len(nums)

        for num in range(2 ** n):
            comb = []
            for index in range(n):
                if index == num:
                    break
                if num & (1 << index )!= 0:
                    comb.append(nums[index])
            result.append(comb.copy())
        return result
