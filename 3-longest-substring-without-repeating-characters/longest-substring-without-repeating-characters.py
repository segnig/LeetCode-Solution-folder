class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = defaultdict(int)

        result = 0

        left, right = 0, 0

        while right < len(s):
            while store[s[right]] > 0:
                store[s[left]] -= 1
                left += 1

            store[s[right]] += 1
            right += 1
            result = max(result, right  - left)

        return result