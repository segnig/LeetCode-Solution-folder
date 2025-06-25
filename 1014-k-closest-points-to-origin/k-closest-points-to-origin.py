class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_distance = []

        for x, y in points:
            points_distance.append((x**2 + y**2, ([x, y])))

        points_distance.sort()

        points_distance = points_distance[:k]
        return [point for dist, point in points_distance]
        