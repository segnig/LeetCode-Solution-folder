class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum_array = [0]
        for num in nums:
            prefix_sum_array.append(prefix_sum_array[-1] + num)

        store = defaultdict(int)
        result = 0
        for num in prefix_sum_array:
            result += store[num - goal]
            store[num] += 1

        return result