class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        result = 0
        store = []

        for i, row in enumerate(grid):
            temp = 0
            row = [-num for num in row]
            heapify(row)
            for _ in range(limits[i]):
                store.append(heappop(row))
        heapify(store)
        for _ in range(k):
            result -= heappop(store)

        return result