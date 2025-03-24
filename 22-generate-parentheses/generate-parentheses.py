class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.generator(n)
        return self.result
        
    def generator(self, n, opened=0, closed=0, stack=[]):
        if opened == closed == n:
            self.result.append("".join(stack))
            return
        if opened < n:
            stack.append("(")
            self.generator(n, opened +1, closed, stack)
            stack.pop()

        if closed < opened:
            stack.append(")")
            self.generator(n, opened, closed + 1, stack)
            stack.pop()
