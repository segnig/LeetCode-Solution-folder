class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        store = set(nums)

        for num in nums:
            reversed_num = int(str(num)[::-1])
            store.add(reversed_num)
        
        return len(store)