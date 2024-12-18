class Solution(object):
    def finalPrices(self, prices):
        result = []

        for i in range(len(prices)):
            temp = prices[i]
            temps = []
            for j in range(i + 1, len(prices)):
                if prices[i] >= prices[j]:
                    temps.append(prices[j])

            temp = prices[i] - temps[0] if temps else temp

            result.append(temp)
        return result