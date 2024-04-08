class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        cT, win = {}, {}
        index = []
        resL = len(s) + 1
        left = 0
        
        for char in t:
            cT[char] = 1 + cT.get(char, 0)

        have, need = 0, len(cT)

        for right in range(len(s)):
            if s[right] in cT:
                win[s[right]] = 1 + win.get(s[right], 0)

                if win[s[right]] == cT[s[right]]:
                    have += 1

            while need == have:
                if right - left + 1 < resL:
                    resL = right - left + 1
                    index = [left, right + 1]

                if s[left] in cT:
                    win[s[left]] -= 1
                    if win[s[left]] < cT[s[left]]:
                        have -= 1
                left += 1

        return s[index[0]:index[1]] if resL < len(s) + 1 else ""