class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        num_ices = 0

        for cost in costs:
            if cost <= coins:
                num_ices += 1
                coins -= cost

        return num_ices