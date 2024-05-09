class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        result = 0
        for i in range(len(happiness)):
            if k == i:
                break
            if i < happiness[i]:
                result += happiness[i] - i
        return  result