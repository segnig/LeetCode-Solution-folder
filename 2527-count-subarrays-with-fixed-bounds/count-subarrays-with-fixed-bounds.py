class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        out_window_index, max_index, min_index = -1, -1, -1
        result = 0

        for index, val in enumerate(nums):
            if val == maxK:
                max_index = index
            if val == minK:
                min_index = index
            if val < minK or maxK < val:
                out_window_index = index
            result += max(0, min(max_index, min_index) - out_window_index)
        return result