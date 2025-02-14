class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        window = Counter()
        res = s
        left = 0
        for right in range(len(s)):
            window[s[right]] += 1
            while self.helper(target, window):
                if len(res) > right - left + 1:
                    res = s[left:right + 1]
                window[s[left]] -= 1
                left += 1
        result_counter = Counter(res)
        return res if self.helper(target, result_counter) else ""

    def helper(self, target, window):
        return target - window == Counter()