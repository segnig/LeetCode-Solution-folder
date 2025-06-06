class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = set()
        canditates = set()

        for i in range(10, len(s) + 1):
            cand = s[i-10:i]
            if cand in canditates:
                result.add(cand)
            canditates.add(cand)

        result = list(result)
        return result