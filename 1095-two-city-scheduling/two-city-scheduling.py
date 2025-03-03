class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[1] - x[0])
        result = 0
        for index, cost in enumerate(costs):
            if index < len(costs) // 2:
                result += costs[index][1]
            else:
                result += costs[index][0] 
        return result