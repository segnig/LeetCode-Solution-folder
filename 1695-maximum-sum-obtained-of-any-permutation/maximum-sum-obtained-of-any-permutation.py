class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        requests_freq = [0 for _ in range(len(nums) + 1)]

        for a, b in requests:
            requests_freq[a] += 1
            requests_freq[b + 1] -= 1
    

        for i in range(1, len(requests_freq)):
            requests_freq[i] += requests_freq[i - 1]
        nums.sort(reverse=True)
        requests_freq.sort(reverse=True)

        result = 0
        for i in range(len(nums)):
            result += nums[i] * requests_freq[i]

        return result % (10**9 + 7)
        