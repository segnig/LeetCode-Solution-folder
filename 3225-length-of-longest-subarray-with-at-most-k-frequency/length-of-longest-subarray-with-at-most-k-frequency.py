class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        counter = defaultdict(int)
        left = 0
        result = 0
        right = 0
        while right < len(nums):
            counter[nums[right]] += 1
            if counter[nums[right]] > k:
                while nums[left] != nums[right]:
                    counter[nums[left]] -= 1 
                    left += 1
                counter[nums[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
            right += 1
        return result
          

        return result