class Solution(object):
    def firstUniqChar(self, s):
        counter_s = Counter(s)

        for i, char in enumerate(s):
            if counter_s[char] == 1:
                return i
        return-1

        