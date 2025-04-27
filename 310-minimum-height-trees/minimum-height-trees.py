class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        indegree = [0] * n

        graph = defaultdict(list)
        number_of_edgee = 0
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
            number_of_edgee += 1

        queue = deque()

        for node, val in enumerate(indegree):
            if val == 1:
                queue.append(node)

        while number_of_edgee > 1:
            for _ in range(len(queue)):
                node = queue.popleft()
                number_of_edgee -= 1

                for nb in graph[node]:
                    indegree[nb] -= 1
                    if indegree[nb] == 1:
                        queue.append(nb)
        


        return list(queue)
        