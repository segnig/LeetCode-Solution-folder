class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        store = set(nums)
        result = []
        for i in range(1, len(nums) + 1):
            if i not in store:
                result.append(i)
        
        return result