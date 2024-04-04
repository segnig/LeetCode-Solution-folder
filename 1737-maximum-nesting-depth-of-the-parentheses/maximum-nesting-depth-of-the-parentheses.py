class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        depth = 0
        for h in s:
            if h == ')':
                if stack:
                    stack.pop()
            elif h == '(':
                stack.append(h)
            depth = max(depth, len(stack))
        return depth 