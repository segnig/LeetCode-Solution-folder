class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num  in range(n+1):
            count = 0
            for bit in range(32):
                count += num & (1 << bit) != 0
            
            res.append(count)

        return res