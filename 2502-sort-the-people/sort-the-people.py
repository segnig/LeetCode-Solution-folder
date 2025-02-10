class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        right = len(heights)

        for j in range(right):
            for i in range(j, 0, -1):
                if heights[i] > heights[i - 1]:
                    heights[i], heights[i - 1] = heights[i - 1], heights[i]
                    names[i], names[i - 1] = names[i - 1], names[i]

        return names           