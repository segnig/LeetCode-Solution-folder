class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        window = Counter()
        res = []
        remain_char = len(target)
        left = 0
        for right in range(len(s)):
            window[s[right]] += 1
            if window[s[right]] == target[s[right]]:
                remain_char -= 1
            while not remain_char:
                if not res or res[1] - res[0] > right - left:
                    res = [left, right]
                window[s[left]] -= 1
                if window[s[left]] + 1 == target[s[left]]:
                    remain_char += 1
                left += 1
        return s[res[0]:res[1] + 1] if res else ""