class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_counter = Counter(nums)

        target = len(nums) / 3

        result = []

        for num in nums_counter:
            if nums_counter[num] > target:
                result.append(num)

        
        return result