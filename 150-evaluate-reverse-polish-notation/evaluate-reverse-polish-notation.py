class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ["+", "-", "/", "*"]:
                right = int(stack.pop())
                left = int(stack.pop())
                if token == "*":stack.append(left * right)
                elif token == "/":stack.append(int(left / right))
                elif token == "+":stack.append(left + right)
                else:stack.append(left - right)
            else:
                stack.append(token)
        return int(stack[0])
