class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")

        paths = [p for p in paths if p]

        stack = []

        for p in paths:
            if p == "..":
                if stack:
                    stack.pop()
            elif p == ".":
                continue
            else:
                stack.append(p)
        return "/" + "/".join(stack)