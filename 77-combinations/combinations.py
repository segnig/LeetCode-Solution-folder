class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = set()
        for i in range(1, n + 1):
            self.generator(n, k, i, [])

        ans = [list(comb) for comb in self.result]

        return ans
        
    def generator(self, n, k, next, comb):
        if len(comb) == k:
            self.result.add(tuple(comb[::]))
            return
        if next > n:
            return
        comb.append(next)
        self.generator(n, k, next + 1, comb)
        comb.pop()
        self.generator(n, k, next + 1, comb)