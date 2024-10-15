class Solution(object):
    def minimumSteps(self, s):
        placed, result, n = 0, 0, len(s)

        for i in range(n - 1, -1, -1):
            if s[i] == "1":
                result += n - i - placed - 1
                placed += 1
        return result

        