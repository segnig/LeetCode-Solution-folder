class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        res = 0
        if y > x:
            for h in s:
                if stack and stack[-1] == 'b' and h == 'a':
                    stack.pop()
                    res += y
                else:
                    stack.append(h)
            s = stack
            stack = []
            for h in s:
                if stack and stack[-1] == 'a' and h == 'b':
                    stack.pop()
                    res += x
                else:
                    stack.append(h)
            
        else:
            for h in s:
                if stack and stack[-1] == 'a' and h == 'b':
                    stack.pop()
                    res += x
                else:
                    stack.append(h)
        
            s = stack
            stack = []
            for h in s:
                if stack and stack[-1] == 'b' and h == 'a':
                    stack.pop()
                    res += y
                else:
                    stack.append(h)
        return res


        