class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append((prefix_sum[-1] + num) % k)

        remain_counter = defaultdict(int)
        result = 0
        for num in prefix_sum:
            result += remain_counter[num]
            remain_counter[num] += 1

        return result