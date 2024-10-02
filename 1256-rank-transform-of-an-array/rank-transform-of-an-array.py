class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        temp = {}

        sorted_arr = sorted(list(set(arr)))
        for i in range(len(sorted_arr)):
            temp[sorted_arr[i]] = i + 1
        
        result = [temp[n] for n in arr]
        return result   