class Solution(object):
    def areOccurrencesEqual(self, s):
        threshold = len(s) // len(set(s))
        counter = Counter(s)

        for char in counter:
            if counter[char] != threshold:
                return False

        return True