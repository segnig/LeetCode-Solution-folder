class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_count = 0
        result = None

        for val, count in counter.items():
            if max_count < count:
                result, max_count = val, count
        
        return result
        