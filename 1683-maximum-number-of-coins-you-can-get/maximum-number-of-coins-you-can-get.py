class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        my_coins = 0
        piles.sort(reverse=True)

        for i in range(1, len(piles)// 3 * 2, 2):
            my_coins += piles[i]

        return my_coins