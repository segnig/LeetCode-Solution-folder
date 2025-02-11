class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # costs.sort()

        # num_ices = 0

        # for cost in costs:
        #     if cost <= coins:
        #         num_ices += 1
        #         coins -= cost

        # return num_ices

        max_cost = max(costs)

        costs_count = [0 for _ in range(max_cost + 1)]
        for c in costs:
            costs_count[c] += 1

        ice_num = 0

        for i in range(1, max_cost + 1):
            q, r = divmod(coins, i)
            num = min(q, costs_count[i])
            ice_num += num
            coins = (q - num) * i + r

        return ice_num