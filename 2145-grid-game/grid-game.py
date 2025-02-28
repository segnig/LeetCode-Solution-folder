class Solution:  
    def gridGame(self, grid: List[List[int]]) -> int:  
        first_row_sum = sum(grid[0])
        second_running_sum = 0
        result = first_row_sum - grid[0][0]

        for index in range(len(grid[0])):
            first_row_sum -= grid[0][index]
            result = min(result, max(second_running_sum, first_row_sum))
            second_running_sum += grid[1][index]
        
        return result
