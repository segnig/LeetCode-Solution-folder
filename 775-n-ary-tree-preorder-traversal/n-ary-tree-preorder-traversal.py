"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.result = []
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if not node:
            return 
        self.result.append(node.val)
        for child in node.children:
            self.dfs(child)
        