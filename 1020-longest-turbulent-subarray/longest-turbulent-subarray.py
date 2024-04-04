class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left, right = 0, 1
        res = 1
        pre = ""

        while right < len(arr):
            if arr[right-1] > arr[right] and pre != ">":
                res = max(res, right - left + 1)
                right += 1
                pre = ">"
            elif arr[right-1] < arr[right] and pre != "<":
                res = max(res, right - left + 1)
                right += 1
                pre = "<"
            else:
                right = right + 1 if arr[right] == arr[right - 1] else right
                left = right - 1
                pre = ""

        return res
