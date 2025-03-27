class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        self.position = sorted(position)
        self.m = m
        left, right = 0, max(position) - min(position)

        while left <= right:
            mid = left + (right - left) // 2
            if self.check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right

    
    def check(self, force):
        last = 0
        current = 0
        for i in range(self.m - 1):
            while current < len(self.position) and self.position[current] - self.position[last] < force:
                current += 1
            if current == len(self.position):
                return False
            last = current
        return True