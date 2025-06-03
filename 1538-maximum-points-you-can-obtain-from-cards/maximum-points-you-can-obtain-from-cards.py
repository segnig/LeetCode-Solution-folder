class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        prefix_sum = [0]
        for card in cardPoints:
            prefix_sum.append(prefix_sum[-1] + card)

        prefix_sum = prefix_sum
        result = prefix_sum[k]
        
        total = prefix_sum[-1]
        for i in range(k):
            result = max(result, prefix_sum[i] + total - prefix_sum[-(k-i+1)])

        return result