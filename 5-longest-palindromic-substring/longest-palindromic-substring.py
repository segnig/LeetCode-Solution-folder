class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            local = ""
            left = i
            right = i
            while left > -1 and right < len(s):
                
                if s[left] !=  s[right]:
                    break
                if right == left:
                    local=s[left]
                else:
                    local = s[left]+local+s[right]
                if len(local)>len(result):
                    result = local
                left-=1
                right += 1
        for i in range(len(s)):
            left = i
            right = i+1
            local = ""
            left = i
            while left > -1 and right < len(s):
                if s[left] !=  s[right]:
                    break
                if right == left:
                    local=s[left]
                else:
                    local = s[left]+local+s[right]
                if len(local)>len(result):
                    result = local
                left-=1
                right += 1
        return result