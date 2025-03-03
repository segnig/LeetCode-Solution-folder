class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        difference = [
            (cost[1] - cost[0], index) for index, cost in enumerate(costs)
        ]
        difference.sort()
        result = 0
        count = 0
        for _, index in difference:
            if count < len(costs) // 2:
                result += costs[index][1]
            else:
                result += costs[index][0] 
            count += 1
        return result