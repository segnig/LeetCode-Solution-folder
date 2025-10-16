class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        valid = set()
        for idx, char in enumerate(s):
            if char in ["(", ")"]:
                if char == "(":
                    stack.append(idx)
                elif stack:
                    pair = stack.pop()
                    valid.add(pair)
                    valid.add((idx))
        
        result = ""
        for idx, char in enumerate(s):
            if char in ["(", ")"]:
                if idx in valid:
                    result += char
            else:
                result += char

        return result