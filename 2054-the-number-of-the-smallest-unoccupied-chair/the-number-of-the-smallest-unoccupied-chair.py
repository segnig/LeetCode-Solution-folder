class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        target = times[targetFriend][0]

        open_ = min([x[0] for x in times])
        close = max([x[1] for x in times]) + 1

        unoccupied = list(range(len(times)))
        leave = []

        heapify(unoccupied)

        times = {a:l for a, l in times}

        for arrival in range(open_, close):
            while leave and arrival == leave[0][0]:
                l, sit = heappop(leave)
                heappush(unoccupied, sit)
            if arrival == target:
                return unoccupied[0]
            if arrival in times:
                sit = heappop(unoccupied)
                heappush(leave, (times[arrival], sit))
