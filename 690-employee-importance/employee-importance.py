"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.id_node = {}

        for node in employees:
            self.id_node[node.id] = node

        for node in employees:
            if node.id == id:
                return self.dfs(self.id_node[id])
        
        return 0

    def dfs(self, node):
        if not node.subordinates:
            return node.importance
            
        result = node.importance
        for nb in node.subordinates:
            result += self.dfs(self.id_node[nb])
        return result