class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        window = Counter()
        res = ""
        remain_char = len(target)
        left = 0
        for right in range(len(s)):
            window[s[right]] += 1
            if window[s[right]] == target[s[right]]:
                remain_char -= 1
            while not remain_char:
                if len(res) > right - left + 1 or not res:
                    res = s[left:right + 1]
                window[s[left]] -= 1
                if window[s[left]] + 1 == target[s[left]]:
                    remain_char += 1
                left += 1
        result_counter = Counter(res)
        return res