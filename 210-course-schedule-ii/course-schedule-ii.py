class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph = [[] for _ in range(numCourses)]
        self.colors = [0 for _ in range(numCourses)]

        self.orders = []
        for course, pre in prerequisites:
            self.graph[pre].append(course)

        for node in range(numCourses):
            if not self.topSort(node):
                return []
        return self.orders[::-1]

    def topSort(self, node):
        if self.colors[node] == 1:
            return False
        
        if self.colors[node] == 2:
            return True
        
        self.colors[node] = 1

        for nb in self.graph[node]:
            if not self.topSort(nb):
                return False
        self.colors[node] = 2
        self.orders.append(node)

        return True