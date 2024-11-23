class Solution(object):
    def findClosestElements(self, arr, k, x):
        result = []

        for i, n in enumerate(arr):
            result.append((abs(x - n), i))

        result.sort()
        res = []
        for i in range(k):
            res.append(arr[result[i][1]])

        res.sort()

        return res
           