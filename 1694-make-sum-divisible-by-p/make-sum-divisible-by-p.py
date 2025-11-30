class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total = 0

        for num in nums:
            total = (total + num) % p

        target = total % p
        if target == 0:
            return 0

        mod_map = {
            0: -1
        }
        current = 0
        min_len = n

    
        for i in range(n):
            current = (current + nums[i]) % p
            needed = (current - target + p) % p
            if needed in mod_map:
                min_len = min(min_len, i - mod_map[needed])
            mod_map[current] = i
            
        return -1 if min_len == n else min_len