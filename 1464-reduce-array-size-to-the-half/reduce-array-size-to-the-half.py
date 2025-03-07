class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        result = 0
        res = 0
        counter = Counter(arr)
        arr = [val for key, val in counter.items()]
        arr.sort(reverse=True)

        for num in arr:
            result += num
            res += 1
            if result >= n//2:
                return res
        
        return res