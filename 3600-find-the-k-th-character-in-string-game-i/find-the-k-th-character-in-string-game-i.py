class Solution:
    def kthCharacter(self, k: int) -> str:
        result = self.helper(k)
        return result[k-1]


    def helper(self, k):
        if k == 0:
            return "a" 
        else:
            result = self.helper(k//2)
            res = ""
            for char in result:
                a = ord("a")
                x = ord(char)
                x += 1 - a
                x %= 26
                res += chr(x + a)
            result = result + res
            return result