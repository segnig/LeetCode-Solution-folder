class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        store = defaultdict(int)
        result = 0
        for num in prefix_sum:
            result += store[num - goal]
            store[num] += 1

        return result