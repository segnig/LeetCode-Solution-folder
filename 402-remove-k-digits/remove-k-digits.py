class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        left = 0
        while left < len(stack):
            if stack[left] != "0":
                break
            left += 1
        if k > 0:
            stack = stack[:-k]

        return "".join(stack[left:]) if stack[left:] else "0" 