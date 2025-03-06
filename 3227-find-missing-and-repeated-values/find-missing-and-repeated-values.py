class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        store = set(
            x for x in range(1, n*n + 1)
        )
        result = [0, 0]

        for i in range(n):
            for j in range(n):
                if grid[i][j] not in store:
                    result[1] = grid[i][j]
                else:
                    store.remove(grid[i][j])
        for x in store:
            result[0] = x

        return result[::-1]
        