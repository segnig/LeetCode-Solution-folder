class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []

        for row in image:
            res = []
            for t in row[::-1]:
                if t == 1:
                    res.append(0)
                else:
                    res.append(1)

            result.append(res)

        return result

        