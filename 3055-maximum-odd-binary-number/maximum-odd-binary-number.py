class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        counter = Counter(s)
        result = "1" * (counter["1"] - 1) + "0" * (counter["0"]) + "1"
        return result