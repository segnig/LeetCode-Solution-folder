class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 2:
            return 0
        k = int(math.log(n) // math.log(5))
        result = 0
        for i in range(1, k +1):
            result += int(n/5 ** i)
            
        return result 