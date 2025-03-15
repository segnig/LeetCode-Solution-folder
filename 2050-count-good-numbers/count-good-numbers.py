class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        result = 1
        result *= pow(5, (n + 1)//2, MOD)
        result *= pow(4, n//2, MOD)
        result %= MOD
        return result