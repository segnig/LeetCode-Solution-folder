class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        result = []

        for hm in timePoints:
            h, m = map(int, hm.split(":"))
            result.append(int(h*60 + m))
            

        result.sort()
        res = 24 * 60
        N = len(result)
        for i in range(N):
            if i == N -1:
                res = min(res, result[0] + 24 * 60 - result[-1])
            else:
                res = min(res, result[i + 1] - result[i])

        return res