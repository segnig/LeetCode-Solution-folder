class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.graph = defaultdict(list)
        

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and i != j:
                    self.graph[i].append(j)

        self.visited = set()
        count = 0
        
        for i in range(len(isConnected)):
            if i not in self.visited:
                count += 1
                self.dfs(i)
                print(i, self.visited)

        return count

    # DFS
    def dfs(self, node):
        if node in self.visited:
            return 
        self.visited.add(node)
        for nb in self.graph[node]:
            self.dfs(nb)