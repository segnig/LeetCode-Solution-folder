class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        w1 = {}
        for i in range(len(s)):
            if s[i] in w1:
                if t[i] != w1[s[i]]:
                    return False
            w1[s[i]] = t[i]
        w1 = {}
        for i in range(len(s)):
            if t[i] in w1:
                if s[i] != w1[t[i]]:
                    return False
            w1[t[i]] = s[i]
        return True

        
        