class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        
        temp = set(stones)
        hashTable = {stone: i for i, stone in enumerate(stones)}

        @cache
        def dp(k, i):
            if i == len(stones) - 1:
                return True
            
            stone = stones[i]
            step1, step2, step3 = False, False, False
            step1 = (k-1 != 0) and (stone + k-1 in temp) and dp(k-1, hashTable[stone + k-1])
            step2 = (k != 0) and (stone + k in temp) and dp(k, hashTable[stone + k])
            step3 = (k+1 != 0) and (stone + k+1 in temp) and dp(k+1, hashTable[stone + k+1])
                    

            return step1 or step2 or step3 

        return dp(1, 1)