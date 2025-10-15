class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq_s = Counter(s)
        freq_t = Counter(t)
        
        
        # bababa = ab
        
        need = 0
        for char in set(s+t):
            need += abs(freq_s[char] - freq_t[char])
        
        return need // 2