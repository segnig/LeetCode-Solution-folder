class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations) - 1
        while left <= right:
            mid = left + (right - left) // 2
            h = len(citations) - mid
            if citations[mid] < h:
                left = mid + 1
            else:
                right = mid - 1

        return len(citations) - left