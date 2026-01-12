class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        x1, y1 = points[0]
        for x, y in points[1:]:
            result += max(abs(x-x1), abs(y-y1))
            x1, y1 = x, y
        
        return result


        