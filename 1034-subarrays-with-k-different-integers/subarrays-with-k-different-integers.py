class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        def solver(nums: List[int], k: int):
            left, right, n = 0 , 0, len(nums)
            res = 0
            store = defaultdict(int)
            while right < n:
                store[nums[right]] += 1
                while len(store) > k:
                    store[nums[left]] -= 1
                    if store[nums[left]] == 0:
                        del store[nums[left]]
                    left += 1
                res  += right + 1 - left
                right += 1

            return res
        return solver(nums, k) - solver(nums, k - 1)
        