class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        for vertex in range(len(graph)):
            if not self.bfs(graph, vertex):
                return False
        return True


    def bfs(self, graph, start):
        colors = [-1] * len(graph)
        queue = deque([start])
        colors[start] = 1
        while queue:
            parent = queue.popleft()
            color = 1 - colors[parent]

            for child in graph[parent]:
                if colors[child] == -1:
                    colors[child] = color
                    queue.append(child)
                elif colors[child] != color:
                    return False

        return True