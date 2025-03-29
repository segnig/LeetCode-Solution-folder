class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        left = 0
        right = max(houses + heaters)
        houses.sort()
        heaters.sort()

        while left <= right:
            mid = left + (right - left)// 2
            if self.canCover(houses, heaters, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def canCover(self, houses, heaters, radius):
        index = 0
        for i in range(len(houses)):
            while index < len(heaters) and abs(houses[i] - heaters[index]) > radius:
                index += 1
            if index == len(heaters):
                return False
        return True
