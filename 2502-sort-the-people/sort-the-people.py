class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        heights_name = [(val, names[index]) for index, val in enumerate(heights)]
        

        right = len(heights)

        while right > 0:
            for i in range(right - 1):
                if heights_name[i][0] < heights_name[i + 1][0]:
                    heights_name[i], heights_name[i+1] = heights_name[i+1], heights_name[i]

            right -= 1
            

        return [person[1] for person in heights_name]            

