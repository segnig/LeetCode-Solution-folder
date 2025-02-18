class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        paths = [0 for _ in range(1000 + 2)]
        for p, a, b in trips:
            paths[a] += p
            paths[b] -= p
        temp = 0
        for n in paths:
            if temp + n > capacity:
                return False
            temp += n
        return True