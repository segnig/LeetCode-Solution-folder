class Solution(object):
    def numberOfSubarrays(self, nums, k):
        is_odd = []
        for x in nums:
            if x % 2 == 0:
                is_odd.append(0)
            else:
                is_odd.append(1)
        prefix_sum = [0]

        for x in is_odd:
            prefix_sum.append(prefix_sum[-1] + x)

        counts = []
        cc = Counter(prefix_sum)
        for v, c in cc.items():
            counts.append((v, c))


        left, right = 0, 0

        res = 0

        while right < len(counts):
            if counts[right][0] - counts[left][0] > k:
                left += 1
            if counts[right][0] - counts[left][0] == k:
                res += counts[right][1] * counts[left][1]
                left += 1
            right += 1

        return res