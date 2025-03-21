class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.result = set()
        self.indeies = set()
        self.generator(tiles, [])
        print(self.result)
        return len(self.result) - 1

    def generator(self, nums, comb):
        if len(comb) <= len(nums):
            self.result.add("".join(comb[:]))
        
        if len(comb) == len(nums):
            return
        
        for i in range(len(nums)):
            if i not in self.indeies:
                comb.append(nums[i])
                self.indeies.add(i)
                self.generator(nums, comb)
                self.indeies.remove(i)
                comb.pop()
        