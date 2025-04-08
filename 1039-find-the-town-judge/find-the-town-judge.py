class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        degree = defaultdict(int)

        # let say Degree = Indegree - OutDegree

        for s, d in trust:
            degree[s] -= 1
            degree[d] += 1
        
        for node in range(1, n+1):
            if degree[node] == n - 1:
                return node
        return -1