class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.helper(s) or self.helper(s[::-1])

    def helper(self, s):
        k = 1
        right = len(s) - 1
        left = 0
        while right > left:
            if s[left] != s[right]:
                if k == 0:
                    return False
                left += 1
                k -= 1
            else:
                right, left = right -1, left + 1
        return True