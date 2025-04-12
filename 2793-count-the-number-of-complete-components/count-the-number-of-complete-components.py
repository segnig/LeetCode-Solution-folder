class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        self.graph = defaultdict(list)
        result = 0
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        
        self.visited = set()
        
        for node in range(n):
            if node not in self.visited:
                self.component = []
                self.dfs(node)
                is_completed = True
                for com in self.component:
                    if len(self.graph[com]) != len(self.component) - 1:
                        is_completed = False
                        break
                if is_completed:
                    result += 1
        return result

    def dfs(self, node):
        self.visited.add(node)
        self.component.append(node)
        for nb in self.graph[node]:
            if nb not in self.visited:
                self.dfs(nb) 