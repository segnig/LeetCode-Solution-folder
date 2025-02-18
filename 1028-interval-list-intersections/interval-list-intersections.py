class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        top = bottom = 0
        
        while top < len(firstList) and bottom < len(secondList):
            if firstList[top][0] > secondList[bottom][1]:
                bottom += 1
            elif firstList[top][1] < secondList[bottom][0]:
                top += 1
            else:
                result.append([max(firstList[top][0], secondList[bottom][0]), min(firstList[top][1], secondList[bottom][1])])

                if firstList[top][1] > secondList[bottom][1]:
                    bottom += 1
                else: 
                    top += 1
        return result