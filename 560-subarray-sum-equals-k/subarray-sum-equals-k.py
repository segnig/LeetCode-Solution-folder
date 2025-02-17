class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        store = defaultdict(int)
        store[0] = 1

        for num in nums:
            prefix_sum += num
            count += store[prefix_sum - k]
            store[prefix_sum] += 1

            

        return count