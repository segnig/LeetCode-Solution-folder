class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.graph = defaultdict(list)
        self.visited = set()
        self.destination  = destination
        for s, dest in edges:
            self.graph[s].append(dest)
            self.graph[dest].append(s)
        
        return self.dfs(source)
        
    def dfs(self, node):
        if self.destination == node:
            return True
        
        self.visited.add(node)
        
        for nb in self.graph[node]:
            if nb not in  self.visited:
                found = self.dfs(nb)
                if found:
                    return True
        return False
