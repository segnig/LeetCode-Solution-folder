class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1] * len(graph)
        for vertex in range(len(graph)):
            if colors[vertex] == -1:
                if not self.bfs(graph, vertex, colors):
                    return False
        return True


    def bfs(self, graph, start, colors):
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