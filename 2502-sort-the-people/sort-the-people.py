class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        min_h = min(heights)
        max_h = max(heights)

        paired = defaultdict(list)

        heights = [h - min_h  for h in heights]
        order_feq = [0 for _ in range(min_h, max_h + 1)]

        for i in range(len(heights)):
            paired[heights[i]].append(names[i])

        for index in heights:
            order_feq[index] += 1

        result = []
        for index in range(len(order_feq) - 1, -1, -1):
            if order_feq[index] != 0:
                for name in paired[index]:
                    result.append(name)

        return result