class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        s = min(start, destination)
        d = max(start, destination)
        tt = sum(distance[s:d])
        total = sum(distance)
        return min(tt, total - tt)

        