class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter_arr = Counter(arr)
        cnt  = 0
        for chr in arr:
            if counter_arr[chr] == 1:
                cnt += 1
            if cnt == k:
                return chr
        return ""
        