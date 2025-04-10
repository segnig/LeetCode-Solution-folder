class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.graph = defaultdict(list)
        self.informTime = informTime
        self.visited = set()

        self.result = 0
        self.time_taken = self.informTime[headID]

        for i in range(n):
            if manager[i] != -1:
                self.graph[manager[i]].append(i)
        
        self.dfs(headID)
        return self.result


    def dfs(self, node):
        self.visited.add(node)
        for nb in self.graph[node]:
            if nb not in self.visited:
                self.time_taken += self.informTime[nb]
                self.dfs(nb)
                self.result = max(self.result, self.time_taken)
                self.time_taken -= self.informTime[nb]