class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        windows = defaultdict(int)
        result = 1
        left = 0
        windows[s[left]] += 1

        for right in range(1, len(s)):
            while s[right] in windows:
                del windows[s[left]] 
                left += 1
            windows[s[right]] += 1
            result = max(result, right - left + 1)
        return result