class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        right = len(heights)

        for j in range(right):
            max_index = j
            for i in range(j + 1, right):
                if heights[max_index] < heights[i]:
                    max_index = i

            heights[j], heights[max_index] = heights[max_index], heights[j]
            names[j], names[max_index] = names[max_index], names[j]

            

        return names           
