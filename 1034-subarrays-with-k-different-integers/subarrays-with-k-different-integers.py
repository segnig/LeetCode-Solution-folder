class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.solver(nums, k) - self.solver(nums, k - 1)  

    def solver(self, nums, k):
        counter = defaultdict(int)
        left, result = 0, 0

        for right in range(len(nums)):
            counter[nums[right]] += 1
            while len(counter) > k:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
            result += right - left + 1
        
        return result 
