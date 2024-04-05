class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = set(["*", "-", "+", "/"])
        stack = []
        for i in tokens:
            if i in operator:
                a = stack.pop()
                b = stack.pop()
                stack.append(str(int(eval(b+i+a))))
            else:
                stack.append(i)
        print(stack)
        res = round(float(stack[0]))
        return res