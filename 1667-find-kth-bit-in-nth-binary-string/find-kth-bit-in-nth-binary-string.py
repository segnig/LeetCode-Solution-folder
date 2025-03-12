class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        result = self.helper(n) 
        return result[k-1] 


    def helper(self, n):
        if n == 1:
            return "0"
        else:
            res = self.helper(n - 1)
            inverted = "".join("1" if char == "0" else "0" for char in res)
            res += "1" + inverted[::-1]
            return res

