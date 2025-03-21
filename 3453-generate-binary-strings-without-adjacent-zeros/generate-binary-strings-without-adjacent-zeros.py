class Solution:
    def validStrings(self, n: int) -> List[str]:
        self.result = []
        self.backtrack(n)
        return self.result 
    
    def backtrack(self, n,  comb=[]):
        if n == len(comb):
            self.result.append("".join(comb)) 
            return

        if not comb:
            self.backtrack(n, comb + ["1"])
            self.backtrack(n, comb + ["0"])

        else:
            self.backtrack(n, comb + ["1"])
            if comb[-1] != "0":
                self.backtrack(n, comb +["0"])