class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        window = Counter()
        res = s
        poss = len(target)
        left = 0
        for right in range(len(s)):
            window[s[right]] += 1
            if window[s[right]] == target[s[right]]:
                poss -= 1
            while not poss:
                if len(res) > right - left + 1:
                    res = s[left:right + 1]
                window[s[left]] -= 1
                if window[s[left]] + 1 == target[s[left]]:
                    poss += 1
                left += 1
        result_counter = Counter(res)
        return res if self.helper(target, result_counter) else ""

    def helper(self, target, window):
        return target - window == Counter()