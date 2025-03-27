class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.result = []
        self.s = s
        self.backtrack()
        return self.result

    def backtrack(self, index=0, part=[]):
        if len(part) == 4 and index >= len(self.s):
            self.result.append(".".join(part))
            return

        if len(part) > 4:
            return 

        for i in range(index, min(index + 3, len(self.s))):
            sub_str = self.s[index:i+1]
            
            if int(sub_str) <= 255 and (sub_str[0] != '0' or len(sub_str) == 1):
                part.append(sub_str)
                self.backtrack(i+1, part)
                part.pop()