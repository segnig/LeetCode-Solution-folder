class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indexs = {}
        for i, val in enumerate(s):
            indexs[val] = i
        result = []
        for val in s:
            result.append(indexs[val])

        answer = []
        mx = result[0]
        last_indx = -1
        for index, num in enumerate(result):
            mx = max(mx, num)
            if index == mx:
                answer.append(index - last_indx)
                last_indx = index

            
        

        return answer