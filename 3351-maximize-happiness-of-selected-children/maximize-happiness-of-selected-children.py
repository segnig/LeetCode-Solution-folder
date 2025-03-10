class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        result = 0
        for i in range(k):
            result += happiness[i] - i if happiness[i] - i > 0 else 0
        return result