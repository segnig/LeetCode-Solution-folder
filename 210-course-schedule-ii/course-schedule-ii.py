class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegrees[course] += 1

        queue = deque()
        orders = []

        for course in range(numCourses):
            if indegrees[course] == 0:
                queue.append(course)
                orders.append(course)

        while queue:
            node = queue.popleft()

            for nb in graph[node]:
                indegrees[nb] -= 1
                if indegrees[nb] == 0:
                    queue.append(nb)
                    orders.append(nb)
        
        if len(orders) < numCourses:
            return []
        
        return orders

