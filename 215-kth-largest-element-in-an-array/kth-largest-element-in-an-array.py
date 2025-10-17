class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        result = []

        for num in nums:
            if len(result) == k:
                if result[0] < num:
                    heappop(result)
                    heappush(result, num)

            else:
                heappush(result, num)
            
        return result[0]