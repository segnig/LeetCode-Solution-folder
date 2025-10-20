class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)

        for index, char in enumerate(s):
            if counter[char] == 1:
                return index

        return -1        