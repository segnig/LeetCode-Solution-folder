class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        result = [0]

        for par in s:
            if par == "(":
                result.append(0)
            else:
                top = result.pop()
                if top == 0:
                    result[-1] += 1
                else:
                    result[-1] += 2 * top
        return result[-1]