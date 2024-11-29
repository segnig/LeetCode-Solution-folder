class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        res = 1
        left, right = 0, 1

        while right < len(s):
            while right < len(s) and ord(s[left]) + right - left == ord(s[right]):
                right += 1
                res = max(res, right - left)
            else:
                left, right = right, right + 1
            
        return res