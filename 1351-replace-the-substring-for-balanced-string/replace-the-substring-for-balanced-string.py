class Solution:
    def balancedString(self, s: str) -> int:
        counter = Counter(s)
        over = Counter()
        for char in counter:
            if counter[char] > len(s)// 4:
                over[char] = counter[char] - len(s)// 4
        if not over:
            return 0
        
        window = defaultdict(int)
        left = 0
        res = len(s)
        for right in range(len(s)):
            window[s[right]] += 1
            while left <= right and  self.helper(over, window):
                print(window, over)
                window[s[left]] -= 1
                res = min(res, right - left + 1) 
                left += 1
                

        return res

    def helper(self, over, window):
        for c in over:
            if window[c] < over[c]:
                return False
        return True