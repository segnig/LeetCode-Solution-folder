class Solution(object):
    def findScore(self, nums):
        stores = [(v, i) for i, v in enumerate(nums)]
        score = 0
        stores.sort()

        marked = set()

        for v, i in stores:
            if i not in marked:
                score += v
                marked.add(i + 1)
                marked.add(i - 1)
                marked.add(i)


        print(stores)

        return score
        