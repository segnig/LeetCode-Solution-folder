class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        counter = [[counter[key], key] for key in counter]
        counter.sort(reverse=True)
        res = ""

        for char in counter:
            res += char[1] * char[0]

        return res