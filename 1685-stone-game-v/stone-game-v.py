class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:

        @lru_cache(None)
        def dfs(left, right):
            if left == right:
                return 0

            total, ans, sum_left = sum(stoneValue[left:right + 1]), 0, 0

            for i in range(left, right):
                sum_left += stoneValue[i]
                sum_right = total - sum_left

                if sum_left > sum_right:
                    ans = max(ans, dfs(i + 1, right) + sum_right)
                
                elif sum_right > sum_left:
                    ans = max(ans, dfs(left, i) + sum_left)

                else:
                    ans = max(ans, max(dfs(left, i), dfs(i + 1, right)) + sum_left)

            return ans
        
        return dfs(0, len(stoneValue) - 1)
                