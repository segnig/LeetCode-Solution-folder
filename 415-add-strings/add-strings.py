class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""

        remainder = 0

        num1, num2 = num1[::-1], num2[::-1]

        for i in range(max(len(num1), len(num2))):
            a =  int(num1[i]) if i < len(num1) else 0
            b =  int(num2[i]) if i < len(num2) else 0

            result += str((a + b + remainder) % 10)
            remainder = (a + b + remainder) // 10

        if remainder:
            result += str(remainder)

        return result[::-1]
