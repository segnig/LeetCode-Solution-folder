# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        def bfs(root):
            visited = set([root])
            result = [root]
            que = deque([root])
            if root:
                answer.append([root.val])
            while que:
                res = []
                for i in range(len(que)):
                    node = que.popleft()
                    if node:
                        if node.left:
                            visited.add(node.left)
                            que.append(node.left)
                            res.append(node.left.val)
                        if node.right:
                            visited.add(node.right)
                            que.append(node.right)
                            res.append(node.right.val)
                if res:
                    answer.append(res)
        bfs(root)
        return answer

