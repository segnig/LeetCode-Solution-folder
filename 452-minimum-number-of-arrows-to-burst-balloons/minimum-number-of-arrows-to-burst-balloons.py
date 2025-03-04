class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ends = float("inf")
        result = 0

        for start, end in points:
            if start > ends:
                ends = end
                result += 1
            ends = min(ends, end)
        return result + 1