class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0

        for i, cite in enumerate(citations):
            if cite >= i + 1:
                h = i + 1

            else: return h

        return h   
        