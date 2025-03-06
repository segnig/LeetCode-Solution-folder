class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ["+", "-", "/", "*"]:
                right = stack.pop()
                left = stack.pop()
                stack.append(
                    str(int(eval(left + token + right)))
                )
            else:
                stack.append(token)
        return int(stack[0])
