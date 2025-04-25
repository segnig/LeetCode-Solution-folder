class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)

        for pre, course in prerequisites:
            graph[pre].append(course)

        reachable = [set() for _ in range(numCourses)]

        for course in range(numCourses):
            visited = set()
            queue = deque([course])
            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        reachable[course].add(neighbor)
                        queue.append(neighbor)


        return [v in reachable[u] for u, v in queries]
