class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 1
        right = min(ranks) * (cars * cars)
        while left <= right:
            mid = left + (right - left)// 2
            if self.finder(ranks, mid, cars):
                right = mid - 1
                best = mid
            else:
                left = mid + 1
        return left
    
    def finder(self, ranks, time, cars):
        repaired_cars = 0
        for r in ranks:
            repaired_cars += int(sqrt(time/r))
        return repaired_cars >= cars