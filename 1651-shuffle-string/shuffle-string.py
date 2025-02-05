class Solution(object):
    def restoreString(self, s, indices):
        result = ["*" for _ in  range(len(indices))]

        for i, indx in enumerate(indices):
            result[indx] = s[i]

        return "".join(result)
        