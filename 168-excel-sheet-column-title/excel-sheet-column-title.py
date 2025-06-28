class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber:

            result += chr((columnNumber - 1) % 26 + ord("A"))
            columnNumber = (columnNumber - 1) // 26

        return result[::-1]