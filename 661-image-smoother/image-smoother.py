class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        rows, cols = len(img), len(img[0])
        result = [[0 for _ in range(cols)]  for p in range(rows)]

        for r in range(rows):
            for c in range(cols):
                res = 0
                cords = self.helper(rows, cols, r, c)
                for i, j in cords:
                    res += img[i][j]
                
                result[r][c] = int(res/ len(cords))

        return result



    def helper(self, rows, cols, r, c):
        cords = []
        for i in (r- 1, r, r + 1):
            if i >= 0 and i < rows:
                for j in (c- 1, c, c + 1):
                    if j >= 0 and j < cols:
                        cords.append((i, j))
        
        return cords  