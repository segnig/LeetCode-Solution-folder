class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = Counter(s)
        even = [value for value in hm.values() if value % 2 == 0]
        odd = [value for value in hm.values() if value % 2 != 0]
        if odd: 
            use_odds = sum(odd) - (len(odd) - 1) 
            return sum(even) + use_odds
        else: 
            return sum(even)