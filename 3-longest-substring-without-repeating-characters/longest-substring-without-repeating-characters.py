class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        left = 0
        right = 0
        res = 0
        while right < len(s):
            if s[right] in count:
                del count[s[left]]
                left += 1
            else:
                count[s[right]] = 1
                res = max(res, right - left + 1)
                right += 1
        return res