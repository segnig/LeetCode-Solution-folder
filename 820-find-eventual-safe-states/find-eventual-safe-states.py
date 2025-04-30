class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        queue = deque()
        sfate_nodes = []

        temp_graph = [[] for _ in range(len(graph))]
        

        indegrees = [0 for i in range(len(graph))]
        for node in range(len(graph)):
            for nb in graph[node]:
                temp_graph[nb].append(node)
                indegrees[node] += 1

        graph = temp_graph.copy()

        for course in range(len(graph)):
            if indegrees[course] == 0:
                queue.append(course)
                sfate_nodes.append(course)

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for nb in graph[node]:
                    indegrees[nb] -= 1
                    if indegrees[nb] == 0:
                        queue.append(nb)
                        sfate_nodes.append(nb)
    

        return sorted(sfate_nodes)