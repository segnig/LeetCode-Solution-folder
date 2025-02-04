class Solution(object):
    def minSteps(self, s, t):
        counter_s = defaultdict(int)
        counter_t = defaultdict(int)

        for i in range(len(t)):
            counter_t[t[i]] += 1
            counter_s[s[i]] += 1
            
        res = 0
        for k in counter_s:
            if counter_s[k] > counter_t[k]:
                res += counter_s[k] - counter_t[k]

        return res