class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        s_counter = Counter(s)
        t_counter = Counter(t)

        for char in s_counter:
            if s_counter[char] != t_counter[char]:
                return False

        return True      