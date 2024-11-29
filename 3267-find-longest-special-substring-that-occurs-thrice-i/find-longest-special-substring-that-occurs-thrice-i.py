class Solution:
    def maximumLength(self, s: str) -> int:
        hash_table = {}

        for i in range(len(s)):
            for j in range(len(s) + 1):
                if len(set(s[i:j])) == 1:
                    temp = s
                    hash_table[s[i:j]] = 0
                    while temp.find(s[i:j]) != -1:
                        hash_table[s[i:j]] += 1
                        temp = temp[temp.find(s[i:j]) + 1:]

        res = -1
        print(hash_table)

        for sub in hash_table:
            if hash_table[sub] >= 3:
                res = max(res, len(sub))
        
        return res
        