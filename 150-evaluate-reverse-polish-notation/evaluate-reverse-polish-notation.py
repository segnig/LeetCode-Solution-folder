class Solution:
    def resolves(self, a, b, Operator):
        if Operator == '+':
            return a + b
        elif Operator == '-':
            return a - b
        elif Operator == '*':
            return a * b
        return int(a / b)
    def evalRPN(self, tokens: List[str]) -> int:
        operator = set(["*", "-", "+", "/"])
        stack = []
        for i in tokens:
            if i in operator:
                a = stack.pop()
                b = stack.pop()
                stack.append(self.resolves(b, a, i))
            else:
                stack.append(int(i))
        return stack[0]