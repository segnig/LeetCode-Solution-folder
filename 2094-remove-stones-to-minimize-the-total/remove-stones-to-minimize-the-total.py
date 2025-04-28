class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapify(piles)

        for i in range(k):
            pile = - heappop(piles)
            heappush(piles, round(- pile//2))

        return -sum(piles)