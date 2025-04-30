class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)

        graph = [[] for _ in range(n)]

        for u, v in richer:
            graph[v].append(u)

        result = [None] * n

    
        def dfs(node):
            if result[node] is None:
                result[node] = node
                for nb in graph[node]:
                    temp = dfs(nb)

                    if quiet[temp] < quiet[result[node]]:
                        result[node] = temp
            return result[node]

        for node in range(n):
            result[node] = dfs(node)
        
        return result
                        
       