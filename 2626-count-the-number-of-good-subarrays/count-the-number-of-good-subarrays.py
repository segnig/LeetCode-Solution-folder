class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        same, right = 0, -1

        counter = defaultdict(int)
        result = 0

        for left in range(n):
            while same < k and right +1 < n:
                right += 1
                same += counter[nums[right]]
                counter[nums[right]] += 1
            if same >= k:
                result += n - right
            
            counter[nums[left]] -= 1
            same -= counter[nums[left]]
        return result
