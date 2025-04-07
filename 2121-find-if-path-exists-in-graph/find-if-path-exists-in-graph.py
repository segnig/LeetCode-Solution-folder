class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = defaultdict(list)

        for s, dest in edges:
            graph[s].append(dest)
            graph[dest].append(s)
        
        stack = [source]
        visited = set([source])

        while stack:
            node = stack.pop()
            for neighbour in graph[node]:
                if neighbour == destination:
                    return True
                if neighbour not in visited:
                    stack.append(neighbour)
                    visited.add(neighbour)
        
        return False