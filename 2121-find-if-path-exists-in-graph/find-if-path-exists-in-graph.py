class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        print(graph)
        def bfs(src, des):
            if src == des:
                return True
            visited = set([src])
            que = deque([src])
            while que:
                node = que.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        if neighbor == des:
                            return True
                        que.append(neighbor)
                        visited.add(neighbor)
            return False
        return bfs(source, destination)
        
        