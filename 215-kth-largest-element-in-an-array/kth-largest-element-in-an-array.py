class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        m = len(nums) - k + 1

        heapify(nums)

        for _ in range(m):
            n = heappop(nums)
           
        return n