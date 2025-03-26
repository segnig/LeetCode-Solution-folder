class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        self.n = len(nums)
        self.nums = set(nums)
        return self.backtrack()
        
    
    def backtrack(self, comb=""):
        if len(comb) == self.n:
            copy = "".join(comb[::])
            if "".join(comb) not in self.nums:
                return copy
            return ""

        result = self.backtrack(comb + "1")
        if result != "":
            return result
        return self.backtrack(comb + "0")
