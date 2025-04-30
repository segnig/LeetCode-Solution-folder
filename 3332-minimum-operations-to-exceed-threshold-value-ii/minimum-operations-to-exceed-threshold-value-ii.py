class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        count = 0
        while k > nums[0] and len(nums) > 1:
            min_1 = heappop(nums)
            min_2 = heappop(nums)

            heappush(nums, 2*min_1 + min_2)

            count += 1

        return count