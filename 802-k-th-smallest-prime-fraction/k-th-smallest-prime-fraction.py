class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        result = {}
        for i in range(len(arr) -1):
            for j in range(i +1, len(arr)):
                result[(i, j)] = arr[i] / arr[j]
        result = sorted(result.items(), key=lambda x : x[1])
        a, b = result[k-1][0]
        return [arr[a], arr[b]]
