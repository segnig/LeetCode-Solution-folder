class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        store = set()
        stack = []
        for i in range(len(s)):
            if s[i] == ")" and stack and s[stack[-1]] == "(":
                stack.pop()
            elif s[i] == ')':
                store.add(i)
            elif s[i] == '(':
                stack.append(i)

        for n in stack:
            store.add(n)
            
        result = ""
        for i in range(len(s)):
            if i in store:
                continue
            result += s[i]
        return result