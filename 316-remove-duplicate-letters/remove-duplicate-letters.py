from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        in_stack = set()
        stack = []

        for char in s:
            counter[char] -= 1

            if char in in_stack:
                continue

            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                removed = stack.pop()
                in_stack.remove(removed)

            stack.append(char)
            in_stack.add(char)

        return "".join(stack)
