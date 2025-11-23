class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, - inf, -inf]

        for num in nums:
            temp = dp[:]
            if num % 3 == 0:
                for i in range(3):
                    index = i
                    temp[i] = max(dp[i], dp[index] + num)
            elif num % 3 == 1:
                for i in range(3):
                    index = (i+2) % 3
                    temp[i] = max(dp[i], dp[index] + num)
            else:
                for i in range(3):
                    index = (i+1) % 3
                    temp[i] = max(dp[i], dp[index] + num)
            dp = temp
            print(dp)
        return dp[0]