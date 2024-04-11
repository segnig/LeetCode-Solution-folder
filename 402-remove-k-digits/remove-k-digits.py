class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while stack and  stack[-1] > n and k > 0:
                stack.pop()
                k -= 1
            stack.append(n)
        stack = stack[:-k] if k >0 else stack
        result = "".join(stack).lstrip('0')
        result = result if result else "0"
        return result