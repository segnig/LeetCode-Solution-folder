class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        result = ''
        times = 0
        
        for char in s:
            if char.isdigit():
                times = times * 10 + int(char)
            elif char == '[':
                stack.append((result, times))
                result = ''
                times = 0
            elif char == ']':
                prev_rsult, num = stack.pop()
                result = prev_rsult + num * result
            else:
                result += char
        return result