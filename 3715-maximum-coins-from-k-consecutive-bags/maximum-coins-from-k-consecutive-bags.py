class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        
        def helper(orders):
            orders.sort()

            result, current, index = 0, 0, 0
            for i in range(len(orders)):
                current += (orders[i][1] - orders[i][0] + 1) * orders[i][2]
                while orders[index][1] < orders[i][1] - k + 1:
                    current -= (orders[index][1] - orders[index][0] + 1) * orders[index][2]
                    index += 1
                part = max(0, orders[i][1] - k - orders[index][0] + 1) * orders[index][2]
                result = max(result, current - part)
            return result

        return max(helper(coins), helper([[-r, -l, c] for l, r, c in coins]))