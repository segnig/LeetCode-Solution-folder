class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""

        store = set(s)

        for index, char in enumerate(s):
            if char.swapcase() not in store:
                left_substring = self.longestNiceSubstring(s[:index])
                right_substring = self.longestNiceSubstring(s[index+1:])

                if len(left_substring)  >= len(right_substring):
                    return left_substring
                else:
                    return right_substring
        return s