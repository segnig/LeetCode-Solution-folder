class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graph = defaultdict(list)

        for index, equation in enumerate(equations):
            self.graph[equation[0]].append([equation[1], values[index]])
            self.graph[equation[1]].append([equation[0], 1 / values[index]])

        result = []

        for scr, dest in queries:
            result.append(self.bfs(scr, dest))

        return result

    def bfs(self, source, destination):
        if source not in self.graph or destination not in self.graph:
            return -1

        queue = deque([[source, 1]])
        visited = ([source])

        while queue:
            node, val = queue.popleft()
            if node == destination:
                return val

            for nbr, w in self.graph[node]:
                if nbr not in visited:
                    queue.append([nbr, w * val])
                    visited.append(nbr)
                    
        return -1