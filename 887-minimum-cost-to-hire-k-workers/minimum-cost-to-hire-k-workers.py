class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:

        pair_ratio = []
        
        for i in range(len(quality)):
            pair_ratio.append((wage[i] / quality[i], quality[i]))

        pair_ratio.sort(key= lambda p: p[0])
        heapstore = []
        total_qua = 0
        result = float("inf")

        for rate, qua in pair_ratio:
            heapq.heappush(heapstore, -qua)
            total_qua += qua

            if len(heapstore) > k:
                total_qua += heapq.heappop(heapstore)
            
            if len(heapstore) == k:
                result = min(result, rate * total_qua)

        return result

        