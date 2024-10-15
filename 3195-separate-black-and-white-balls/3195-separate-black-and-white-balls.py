class Solution(object):
    def minimumSteps(self, s):
        placed, result = 0, 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "1":
                result += len(s) - i - placed - 1
                placed += 1
        return result

        