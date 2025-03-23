class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result, stack = [], []
        for index in range(len(pattern) + 1):
            stack.append(index + 1)

            while stack and (index == len(pattern) or pattern[index] == "I"):
                result.append(str(stack.pop()))

        return "".join(result)
