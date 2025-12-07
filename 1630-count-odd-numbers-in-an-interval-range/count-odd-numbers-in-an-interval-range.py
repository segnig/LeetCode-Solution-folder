class Solution:
    def countOdds(self, low: int, high: int) -> int:
        result = (high - low) // 2 + int(low % 2 == 1 or high % 2 == 1)

        return result
        