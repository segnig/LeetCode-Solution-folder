class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        p_count = Counter(p)      
        substring_count = Counter( s[:len(p) - 1])
        left = 0
        ans = []
        for right in range(len(p) - 1, len(s)):  
            substring_count[s[right]] += 1                
            if substring_count == p_count:
                ans.append(left)
            
            substring_count[s[left]] -= 1
            
            if substring_count[s[left]] == 0:
                del substring_count[s[left]]

            left +=1
        return ans