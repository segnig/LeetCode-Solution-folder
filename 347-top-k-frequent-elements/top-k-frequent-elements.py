class Solution(object):
    def topKFrequent(self, nums, k):
        sort_feq = [(f, n) for n, f in Counter(nums).items()]

        sort_feq.sort(reverse=True)

        result = []
        for i in range(k):
            result.append(sort_feq[i][1])

        return result
        