class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        s = [k.strip() for k in s if k]
        result = ""
        for h in range(len(s)-1, -1, -1):
            result += s[h].strip() + " "

        return result.strip() 