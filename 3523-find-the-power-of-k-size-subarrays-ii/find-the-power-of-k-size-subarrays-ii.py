class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        result = []
        best_order = 0
        for i in range(1, k):
            best_order += nums[i-1] - nums[i] == -1
        
        if best_order - k == -1:
            result.append(nums[k-1])
        else:
            result.append(-1)
        
        for i in range(k, len(nums)):
            best_order -= nums[i-k+1] - nums[i-k] == 1
            best_order += nums[i] - nums[i-1] == 1
            if best_order == k -1:
                result.append(nums[i])
            else:
                result.append(-1)

        return result
        