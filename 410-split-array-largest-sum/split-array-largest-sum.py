class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        dp = {}

        def dfs(i , m):
            if m == 1:
                return sum(nums[i:])
            if (i, m) in dp:
                return dp[(i, m)]
            res, curSum = float('inf'), 0
            for j in range(i, len(nums) - m + 1):
                curSum += nums[j]
                maxSum = max(curSum, dfs(j + 1, m - 1))
                res = min(res, maxSum)
                if curSum > res:
                    break
            dp[(i, m)] = res
            return res
        return dfs(0, k)