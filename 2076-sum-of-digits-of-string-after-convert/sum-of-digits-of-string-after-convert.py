class Solution(object):
    def getLucky(self, s, k):
        res = ""
        for char in s:
            res += str(ord(char) - ord("a") + 1)
        while k:
            r = 0
            for c in res:
                r += int(c)
            res = str(r)
            k -= 1

        return int(res)
        