class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []
        self.generator(n, k, 1, [])
        
        return self.result
        
    def generator(self, n, k, next, comb):
        if len(comb) == k:
            self.result.append(comb[::])
            return
        if next > n:
            return
        comb.append(next)
        self.generator(n, k, next + 1, comb)
        comb.pop()
        self.generator(n, k, next + 1, comb)