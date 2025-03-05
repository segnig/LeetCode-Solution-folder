class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in set(["]", ")", "}"]):
                if stack:
                    if stack[-1] == "[" and char == "]":
                        stack.pop()
                    elif stack[-1] == "{" and char == "}":
                        stack.pop()
                    elif stack[-1] == "(" and char == ")":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0