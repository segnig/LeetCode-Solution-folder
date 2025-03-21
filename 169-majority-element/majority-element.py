class Solution(object):
    def majorityElement(self, nums):
        
        count = Counter(nums)
        res = 0
        cur = 0

        for h in count:
            if count[h] > res:
                res = count[h]
                cur = h
        return cur
        