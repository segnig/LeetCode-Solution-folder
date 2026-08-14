class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        ans = 2

        freq_store = defaultdict(int)

        left = 0

        for right in range(len(s)):
            freq_store[s[right]] += 1

            while freq_store[s[right]] > 2:
                freq_store[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)
        
        return ans