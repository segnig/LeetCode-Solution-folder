# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        array = defaultdict(list) # level values

        def bfs(node, level):
            # base case
            if not node: 
                return 

            array[level - 1].append(node.val)
            bfs(node.left, level+1)
            bfs(node.right, level+1)

        bfs(root, 1)

        print(array) #  [[1], [2, 3], [5, 3, 4], [7]]
        
        res = []
        for values in array.values():
            res.append(values[-1])


        return res 