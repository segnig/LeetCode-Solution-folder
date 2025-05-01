class SeatManager:

    def __init__(self, n: int):
        self.unreserved = [_ for _ in range(1, n + 1)]
        heapify(self.unreserved)

    def reserve(self) -> int:
        return heappop(self.unreserved)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.unreserved, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)