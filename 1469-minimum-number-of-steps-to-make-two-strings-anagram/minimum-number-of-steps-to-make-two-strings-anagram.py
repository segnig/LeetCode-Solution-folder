class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """
        s = "bab", t = "aba"
        bababa
        a:3 b:3
        
        s = {b:2, a:1, c:2}  t = {a:3, b:1, c:1} a=2 b=1 c=1 
        need = 2 
        have = 2
        
        s = "leetcode", t = "practice" 
        {l:1, e:3, t:1, o:1, d:1, c:1}    {p:1, c:2, a:1, t:1, i:1, e:1, r:1}
        need=  1 + 2 + 1 + 1
        have=  1 + 1 + 1 + 1 + 1 
        
        """ 
        freq_s = Counter(s)
        freq_t = Counter(t)
        
        
        # bababa = ab
        
        need = 0
        for char in set(s+t):
            need += abs(freq_s[char] - freq_t[char])
        
        return need // 2