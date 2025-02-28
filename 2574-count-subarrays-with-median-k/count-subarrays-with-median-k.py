class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0
        hash_map = defaultdict(int)
        hash_map[0] = 1
        running_sum = 0
        k_index = nums.index(k)
        for i in range(k_index + 1, len(nums)):
            if nums[i] > k:
                running_sum += 1
            else:
                running_sum -= 1
            hash_map[running_sum] += 1

        p = 0
        for i in range(k_index, -1, -1):
            if nums[i] > k:
                p += 1
            if nums[i] < k:
                p -= 1

            result += hash_map[-p] + hash_map[1 - p]

        return result