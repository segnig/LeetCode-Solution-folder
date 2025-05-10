class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        self.visited = set()
        result = 0

        for s in strs:
            if s not in self.visited:
                self.dfs(s, strs)
                result += 1
        
        return result
    
    def dfs(self, s, strs):
        if s in self.visited:
            return 
        
        self.visited.add(s)

        for nbr in strs:
            if self.check(s, nbr):
                self.dfs(nbr, strs)


    def check(self, s, nbr):
        count = 0
        for i in range(len(s)):
            if s[i] != nbr[i]:
                count += 1
            
            if count > 2:
                return False
        return count == 2 or count == 0