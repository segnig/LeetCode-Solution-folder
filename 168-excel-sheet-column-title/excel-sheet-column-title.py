class Solution(object):
    def convertToTitle(self, columnNumber):

        res = ""

        while columnNumber > 0:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            res += chr(65 + remainder)

        print(res)

        return res[::-1]