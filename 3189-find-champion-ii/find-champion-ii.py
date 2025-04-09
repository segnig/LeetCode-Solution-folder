class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
             
        for i in range(n):
            for nb in graph[i]:
                indegree[nb] += 1
        
        result = [i for i in range(n) if indegree[i] == 0]
        print(indegree)
        return result[0] if len(result) == 1 else -1
