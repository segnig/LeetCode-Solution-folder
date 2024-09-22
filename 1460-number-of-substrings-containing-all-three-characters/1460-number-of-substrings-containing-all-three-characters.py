class Solution(object):
    def numberOfSubstrings(self, s):
        lastseen = [-1] * 3
        ans = 0

        for i in range(len(s)):
            lastseen[ord(s[i]) - ord("a")] = i
            ans += 1 + min(lastseen)

        return ans

        