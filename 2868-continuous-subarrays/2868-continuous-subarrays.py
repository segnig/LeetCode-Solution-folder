from sortedcontainers import SortedList  
class Solution(object):
    def continuousSubarrays(self, nums):
        store = SortedList()
        n = len(nums)

        start = 0
        res = 0
        
        for end in range(n):
            store.add(nums[end])

            while store[-1] - store[0] > 2:
                store.remove(nums[start])
                start += 1
            res += end - start + 1

        return res