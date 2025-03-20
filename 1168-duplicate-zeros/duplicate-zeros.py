class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        result = []
        index = 0

        while len(result) < len(arr):
            if arr[index] == 0:
                result.append(arr[index])
                if len(result) < len(arr):
                    result.append(arr[index])
            else:
                result.append(arr[index])
            index += 1
            
        for i in range(len(arr)):
            arr[i] = result[i]