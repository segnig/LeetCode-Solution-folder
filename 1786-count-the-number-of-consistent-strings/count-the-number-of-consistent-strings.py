class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = 0

        for word in words:
            if self.helper(word, allowed):
                res += 1
            print(word, res)

        return res

    
    def helper(self, word, allowed):
        for char in word:
            if char not in allowed:
                return False

        return True
        