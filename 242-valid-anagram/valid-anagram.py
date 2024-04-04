class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t_counter = Counter(t)
        s_counter = Counter(s)

        for k in t_counter:
            if k not in s_counter or t_counter[k] != s_counter[k]:
                return False
        return True