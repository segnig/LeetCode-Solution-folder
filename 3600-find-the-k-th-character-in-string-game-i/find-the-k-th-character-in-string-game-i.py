class Solution:
    def kthCharacter(self, k: int) -> str:
        result = self.helper(k)
        return result[k-1]

    def helper(self, k):
        if k == 0:
            return "a"
        result = self.helper(k//2)
        res = ""
        a = ord("a")
        for char in result:
            x = ord(char)
            x = x - a + 1
            x %= 26
            res += chr(a + x)
        
        return result + res

        