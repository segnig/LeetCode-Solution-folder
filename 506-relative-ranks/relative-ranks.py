class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s = sorted(score, reverse = True)
        result = {}
        
        for i in range(len(s)):
            if i+1 == 1:
                result[s[i]] = "Gold Medal"
            elif i +1 == 2:
                result[s[i]] = "Silver Medal"
            elif i + 1 == 3:
                result[s[i]] = "Bronze Medal"
            
            else:
                result[s[i]] = f"{i+1}"
                
        result = [result[k] for k in score]
        
        return result