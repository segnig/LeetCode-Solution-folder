class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        for i in range(1, rowIndex + 1):
            current = [1] * (i+1)
            for j in range(1, len(prev)):
                current[j] = prev[j-1] + prev[j]
            prev = current
        return prev
