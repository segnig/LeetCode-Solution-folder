class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for par in s:
            if stack and stack[-1] != par and par == ")":
                stack.pop()
            else:
                stack.append(par)
        return len(stack)