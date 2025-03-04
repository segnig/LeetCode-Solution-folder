class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
    


        max_min = [[float("inf")] * len(grid) for _ in range(len(grid))]

        for i in range(len(grid)):
            mx = max(grid[i])
            for j in range(len(grid)):
                max_min[i][j] = mx

        for i in range(len(grid)):
            mx = max([grid[_][i]for _  in range(len(grid))])
            for j in range(len(grid)):
                max_min[j][i] = min(max_min[j][i], mx)


        for _ in max_min:
            print(_)

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                result += abs(max_min[i][j] - grid[i][j])

        return result

        