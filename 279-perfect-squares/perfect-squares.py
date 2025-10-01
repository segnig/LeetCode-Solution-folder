class Solution:
    def numSquares(self, n: int) -> int:
        temp = []

        for i in range(1, int(sqrt(n))+1):
            temp.append(i*i)
        @cache
        def dp(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return inf
            
            min_ = inf
            for num in temp:
                take = 1 + dp(rem - num)
                min_ = min(min_, take)

            return min_
        
        return dp(n)
