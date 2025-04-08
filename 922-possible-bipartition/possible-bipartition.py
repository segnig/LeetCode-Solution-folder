class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.graph = defaultdict(list)
        self.colors = [-1] * n

        for s, d in dislikes:
            self.graph[s].append(d)
            self.graph[d].append(s)
        
        result = True
        for node in range(1, n + 1):
            if self.colors[node-1] == -1:
                self.colors[node-1] = 1
                result = result and self.dfs(node)
        
        return result


    def dfs(self, node):

        temp = True
        for neighbour in self.graph[node]:
            if self.colors[neighbour - 1] == -1:
                if self.colors[node - 1] == 0:
                    self.colors[neighbour - 1] == 1
                else:
                    self.colors[neighbour - 1] = 0
                temp = temp and self.dfs(neighbour)
            elif self.colors[neighbour - 1] == self.colors[node - 1]:
                return False
            
        return temp
