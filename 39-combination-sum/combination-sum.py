class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(i, total, comb):
            if total == target:
                result.append(comb.copy())
                return

            if target < total or i >= len(candidates):
                return 

            comb.append(candidates[i])
            dfs(i, total + candidates[i], comb)
            comb.pop()
            dfs(i+1, total, comb)

        dfs(0, 0, [])
        return result
            
            

        