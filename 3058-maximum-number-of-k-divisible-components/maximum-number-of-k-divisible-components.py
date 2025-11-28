class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        result = 0
        visited = set([0])

        def dfs(node):
            nonlocal result
            total = values[node]

            for nb in graph[node]:
                if nb not in visited:
                    visited.add(nb)
                    total += dfs(nb)

            if total % k == 0:
                result += 1
                return 0 

            return total

        dfs(0)
        return result
