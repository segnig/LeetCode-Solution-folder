class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = {
            key : [[], []] for key in range(n)
        }

        for a, b in redEdges:
            graph[a][0].append(b)
        for a, b in blueEdges:
            graph[a][1].append(b)

        answer = [-1 for _ in range(n)]
        queue = deque([0])
        visited = set([0])
        dist = 0

        def bfs(color=0):
            queue = deque([(0, color)])
            visited = set([(0, color)])
            dist = 0
            while queue:
                for _ in range(len(queue)):
                    node, color = queue.popleft()
                    if answer[node] == -1:
                        answer[node] = dist
                    else:
                        answer[node] = min(dist, answer[node])
                    color = 1 if color == 0 else 0
                    for nb in graph[node][color]:
                        if (nb, color) not in visited:
                            visited.add((nb, color))
                            queue.append((nb, color))
                dist += 1
        bfs(color=0)
        bfs(color=1)
        return answer