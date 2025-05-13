class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num  in range(n+1):
            count = 0
            while num > 0:
                count += num & 1 !=  0
                num >>= 1
            
            res.append(count)

        return res