class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        memo = {}

        def dp(i, j):
            if i >= len(word1) and len(word2) <= j:
                return 0
            
            if i >= len(word1):
                return len(word2) - j
            
            if j >= len(word2):
                return len(word1) - i
            
            
            if (i, j) not in memo:
                if word1[i] != word2[j]:
                    first = 1 + dp(i+1, j)
                    second = 1 + dp(i, j +1)
                    both = 2 + dp(i+1, j+1)
                    memo[(i, j)] = min([first, second, both])
                else:
                    memo[(i, j)] = dp(i+1, j+1)
            
            return memo[(i, j)]

        return dp(0, 0)