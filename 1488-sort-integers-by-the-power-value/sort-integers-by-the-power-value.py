class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        def helper(x):
            count = 0
            while x != 1:
                if x % 2 == 0:
                    x //= 2
                else: 
                    x = 3 * x + 1
                count += 1
            
            return count
        
        num_pows = [(helper(num), num) for num in range(lo, hi+1)]
        num_pows.sort()

        return num_pows[k-1][1]