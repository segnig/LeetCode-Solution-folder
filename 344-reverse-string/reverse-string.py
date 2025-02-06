class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        n = len(s)

        while n // 2 > left:
            s[left], s[n - 1 - left] = s[n - 1 - left], s[left]
            left = left + 1

        return s