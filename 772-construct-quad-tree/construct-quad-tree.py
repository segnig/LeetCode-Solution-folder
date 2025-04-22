"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        self.grid = grid
        return self.building(len(self.grid), 0, 0)

    def building(self, n, row, col):
        allSame = True
        val = self.grid[row][col]

        for i in range(n):
            for j in range(n):
                if self.grid[row + i][col + j] != val:
                    allSame = False
                    break
            if not allSame:
                break

        if allSame:
            return Node(val=bool(val), isLeaf=True)

        n = n // 2
        topLeft = self.building(n, row, col)
        topRight = self.building(n, row, col + n)
        bottomLeft = self.building(n, row + n, col)
        bottomRight = self.building(n, row + n, col + n)

        return Node(
            val=True,  
            isLeaf=False,
            topLeft=topLeft,
            topRight=topRight,
            bottomLeft=bottomLeft,
            bottomRight=bottomRight
        )
