class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = []
        hash_map = {0:-1}

        for i, num in enumerate(nums):
            if not prefix_sum:
                prefix_sum.append(num % k)
            else:
                prefix_sum.append((prefix_sum[-1] + num )% k)
            if prefix_sum[-1] not in hash_map:
                hash_map[prefix_sum[-1]] = i
            elif i - hash_map[prefix_sum[-1]] > 1:
                return True

        return False