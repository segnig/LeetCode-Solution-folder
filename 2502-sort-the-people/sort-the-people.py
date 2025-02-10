class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        

        right = len(heights)

        while right > 0:
            for i in range(right - 1):
                if heights[i] < heights[i + 1]:
                    heights[i], heights[i+1] = heights[i+1], heights[i]
                    names[i], names[i+1] = names[i+1], names[i]

            right -= 1
            

        return names           

