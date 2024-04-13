# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def bfs(root):
            visited = set([root])
            result = [root]
            que = deque([root])
            while que:
                ll = len(que)
                for i in range(len(que)):
                    node = que.popleft()
                    if i == ll -1 and node:
                        answer.append(node.val)
                    if node:
                        if node.left:
                            visited.add(node.left)
                            que.append(node.left)
                        if node.right:
                            visited.add(node.right)
                            que.append(node.right)
                
        bfs(root)
        return answer

