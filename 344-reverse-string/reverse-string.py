class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0

        while len(s) // 2 > left:
            s[left], s[len(s) - 1 - left] = s[len(s) - 1 - left], s[left]
            left = left + 1

        return s