class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        store = {}

        for index, num in enumerate(nums):
            
            second_num = target - num

            if second_num in store:
                return [store[second_num], index]
            store[num] = index