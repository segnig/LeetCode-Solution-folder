class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if not stack:
                stack.append(ch)
            elif abs(ord(ch) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)

        