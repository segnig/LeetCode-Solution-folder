class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count('1') - ( 1 if s[0] == '1' else 0)
        zeros =  0 if s[0] == '1' else 1

        result = ones + zeros
        for i in range(1, len(s) -1):
            if s[i] == '1':
                ones -= 1
            else:
                zeros += 1
            result = max(result, zeros + ones)
        return result