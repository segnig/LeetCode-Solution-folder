class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        result = 0
        if k > 0:
            result = min(k, numOnes)
            k -= result
        if k > 0:
            k -= numZeros
        
        if k > 0:
            result -= k

        return result