class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        counter = Counter([stone % 3 for stone in stones])

        if counter[0] % 2 == 0:
            return bool(counter[1] and counter[2])

        return abs(counter[1] - counter[2]) > 2