class Solution(object):
    def maxCount(self, banned, n, maxSum):
        banned = set(banned)
        result = 0
        count = 0
        for i in range(1, n+1):
            if (maxSum >= result + i) and (i not in banned):
                result += i
                count += 1
            elif i in banned:
                continue
            else:
                return count
            
        return count