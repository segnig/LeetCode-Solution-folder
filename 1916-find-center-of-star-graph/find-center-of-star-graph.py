class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for v, u in edges:
            graph[v].append(u)
            graph[u].append(v)

        n = len(graph) - 1

        for node in graph:
            if len(graph[node]) == n:
                return node
        