class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        stores = defaultdict(int)
        stores[0] = 1
        count = 0
        prefix = 0
        for num in nums:
            prefix += num
            target = prefix - k
            count += stores[target]
            stores[prefix] += 1

        return count