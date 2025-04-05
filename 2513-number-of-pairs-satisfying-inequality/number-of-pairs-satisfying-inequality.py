class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        sorted_list = []
        result = 0
        for i in range(len(nums1)):
            current_diff = nums1[i] - nums2[i]
            count = bisect_right(sorted_list, current_diff + diff)
            result += count
            bisect.insort(sorted_list, current_diff)
        return result