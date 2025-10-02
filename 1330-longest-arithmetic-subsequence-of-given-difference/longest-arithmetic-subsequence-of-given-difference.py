class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        result = 0
        memo = defaultdict(int)
        for num in arr:
            memo[num] = memo[num - difference] + 1
            result = max(result, memo[num])
        return result