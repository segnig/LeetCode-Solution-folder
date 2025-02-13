class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        result = 0
        left = 0
        most_similary = 0
        for right in range(len(s)):
            window[s[right]] += 1
            most_similary = max(most_similary, window[s[right]])
            while (right - left - most_similary) + 1 > k:
                window[s[left]] -= 1
                left += 1
            result = max(right - left, result)
        return max(len(s) - left, result)