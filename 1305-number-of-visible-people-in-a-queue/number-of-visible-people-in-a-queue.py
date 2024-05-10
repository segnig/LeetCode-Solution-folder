class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        stand = []
        for i in range(n - 1, -1, -1):
            while stand and stand[-1] < heights[i]:
                stand.pop()
                ans[i] += 1
            if stand:
                ans[i] += 1
            stand.append(heights[i])
        return ans
        