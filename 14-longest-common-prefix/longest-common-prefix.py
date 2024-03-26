class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_len = min(len(h) for h in strs)

        pre = strs[0][:min_len]
        for word in strs:
            count = 0
            while count < min_len:
                if pre[count] == word[count]:
                    count += 1
                else:
                    break
            pre = pre[:count]
            min_len = count
            if not pre:
                break
        return pre